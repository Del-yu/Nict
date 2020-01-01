# -*-* coding:UTF-8 -*-*
import sys
import time
import socket
import dns.resolver
from conf import Setting
from lib.core.ClassObject import Discover
from concurrent.futures import ThreadPoolExecutor


class DiscoverModule(Discover):
    def __init__(self):
        super().__init__()
        self.description = '检测目标网站开放的端口信息'

    def start_up(self, target):
        if 'physical address' not in target.keys():
            # 解析域名
            resolver = dns.resolver.Resolver()
            resolver.nameservers = ['8.8.8.8', '114.114.114.114']
            target['ip'] = resolver.query(target['domain'], 'A')[0].to_text()
        result_list = []
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task,
                                       [[target['ip'], port] for port in Setting.DEFAULT_PORT_SERVICES.keys()]):
                if future:
                    result_list.append(future)
                char_set = ['\\', '|', '/', '-']
                sys.stdout.write('\r[{}] Please wait a moment.'.format(char_set[int(time.time()) % 4]))
        count = len(result_list)
        if count == 1:
            return 'open port', result_list[0]
        elif count == 0:
            return 'open port', None
        else:
            return 'open port', ', '.join(result_list)

    def thread_task(self, args_list):
        try:
            socket.setdefaulttimeout(2)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((args_list[0], int(args_list[1])))
            s.close()
            if result == 0:
                service = Setting.DEFAULT_PORT_SERVICES[args_list[1]]
                return args_list[1] + ':' + service
            return ''
        except:
            pass
