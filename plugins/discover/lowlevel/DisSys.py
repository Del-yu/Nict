# -*-* coding:UTF-8 -*-*
import re
import sys
import requests
from conf import Setting
from lib.core.ClassObject import Discover


class DiscoverModule(Discover):
    def __init__(self):
        super().__init__()
        self.description = '检测目标网站使用的系统'

    def start_up(self, target):
        sys.stdout.write('\r[-] Please wait a moment.')
        result = self.simple_task(target)
        if result:
            return 'server system', result
        else:
            return 'server system', None

    def simple_task(self, arg):
        try:
            response = requests.get('http://' + arg['domain'], headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            response.encoding = response.apparent_encoding
            target = arg['domain'].split('.')
            result = re.findall('"(http://.*' + target[-2] + '.' + target[-1] + '/.*\..*)"', response.text)[0]
            response = requests.get(result.upper(), headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            if response.status_code == 200:
                return 'Windows'
            else:
                return 'Linux'
        except:
            pass
