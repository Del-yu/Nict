# -*-* coding:UTF-8
import re
import sys
import requests
from conf import Setting
from lib.core.ClassObject import Discover


class DiscoverModule(Discover):
    def __init__(self):
        super().__init__()
        self.description = '获取目标网站首页标题'

    def start_up(self, target):
        sys.stdout.write('\r[-] Please wait a moment.')
        result = self.simple_task(target)
        if result:
            return 'site title', result
        else:
            return 'site title', None

    def simple_task(self, arg):
        try:
            response = requests.get('http://' + arg['domain'], headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            response.encoding = response.apparent_encoding
            if response.status_code == 200:
                title = re.search('<title>(.*?)</title>', response.text, re.I).group(1)
            elif response.status_code == 302:
                title = '302 to %s' % response.url
            else:
                title = response.status_code
            arg['title'] = title.replace('\n', '').replace(' ', '')[:50]
            if len(title) > 25:
                title = title[:25] + '...'
            return title
        except:
            pass
