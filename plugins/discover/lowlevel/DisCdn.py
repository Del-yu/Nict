# -*-* coding:UTF-8
import re
import sys
import time
import requests
from conf import Setting
from lib.core.ClassObject import Discover
from concurrent.futures import ThreadPoolExecutor


class DiscoverModule(Discover):
    def __init__(self):
        super().__init__()
        self.description = '查询目标网站的IP地址'

    def start_up(self, target):
        try:
            response = requests.post('https://ping.chinaz.com/' + target['domain'],
                                     data={"host": target['domain'], "linetype": "电信,多线,联通,移动,海外"})
            guid_list = re.findall('<div id="(.*?)" class="row listw tc clearfix".*>', response.text)
            encode_str = re.search('<input.*id="enkey".*value="(.*?)"', response.text).group(1)
            ip_list = []
            with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
                for future in executor.map(self.thread_task, [[target['domain'], guid, encode_str] for guid in guid_list]):
                    if re.search(r'ip:\'(.*?)\'', future):
                        ip_list.append(re.search(r'ip:\'(.*?)\'', future).group(1))
                    sys.stdout.write('\r[{}] Please wait a moment.'.format(['\\', '|', '/', '-'][int(time.time()) % 4]))
            # IP去重
            ip_list = list(set(ip_list))
            if len(ip_list) > 1:
                return 'cdn', 'true'
            return 'ip address', ip_list[0]
        except:
            pass

    def thread_task(self, arg_list):
        try:
            data = {
                "guid": arg_list[1],
                "host": arg_list[0],
                "ishost": 0,
                "isipv6": 0,
                "encode": "|sJOaB|hM6TLiNERU6OdzbXYrClbv6Ql",
                "checktype": 0,
            }
            response = requests.post(
                'https://ping.chinaz.com/iframe.ashx?t=ping&callback=jQuery111303541976878094748_1577348834073',
                data=data)
            return response.text
        except:
            pass
