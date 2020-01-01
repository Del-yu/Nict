# -*-* coding:UTF-8 -*-*
import re
import sys
import dns.resolver
import requests
from conf import Setting
from lib.core.ClassObject import Discover


class DiscoverModule(Discover):
    def __init__(self):
        super().__init__()
        self.description = '查询目标网站的地理位置'

    def start_up(self, target):
        # 解析域名
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '114.114.114.114']
        ip = resolver.query(target['domain'], 'A')[0].to_text()
        address = self.simple_task(ip)
        sys.stdout.write('\r[{}] Please wait a moment.')
        return 'physical address', address

    def simple_task(self, arg):
        try:
            search_url = 'http://ipaddr.cz88.net/data.php?ip={}'.format(arg)
            response = requests.post(search_url, headers=Setting.DEFAULT_HTTP_HEADERS,
                                     timeout=Setting.Options['timeout'])
            address = re.findall("ShowIPAddr\('.*','(.*?)','.*'\);", response.text)[0]
            return address
        except:
            pass
