# -*-* coding:UTF-8
import sys
import time
import requests
from conf import Setting
from lib.core.ClassObject import Discover
from concurrent.futures import ThreadPoolExecutor


class DiscoverModule(Discover):
    def __init__(self):
        super().__init__()
        self.description = '检测目标站点使用的脚本语言'

    def start_up(self, target):
        result = ''
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task,
                                       [[target['domain'], _] for _ in ['php', 'asp', 'aspx', 'jsp']]):
                if future:
                    result = future
                char_set = ['\\', '|', '/', '-']
                sys.stdout.write('\r[{}] Please wait a moment.'.format(char_set[int(time.time()) % 4]))
        if result:
            return 'script language', result
        else:
            return 'script language', 'static html'

    def thread_task(self, arg_list):
        try:
            response = requests.get('http://' + arg_list[0] + '/index.' + arg_list[1],
                                    headers=Setting.DEFAULT_HTTP_HEADERS, timeout=Setting.Options['timeout'])
            if response.status_code in [200, 301, 302]:
                return arg_list[1]
            return ''
        except:
            pass
