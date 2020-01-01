# -*-* coding:UTF-8
import os
import re
import sys
import time
import json
import hashlib
import requests
from conf import Setting
from collections import Counter
from lib.core.ClassObject import Discover
from concurrent.futures import ThreadPoolExecutor


class DiscoverModule(Discover):
    def __init__(self):
        super().__init__()
        self.description = '检测目标网站使用的CMS'

    def start_up(self, target):
        result_list = []
        with open(os.path.join('data', Setting.DEFAULT_CMS_DICT), 'r', encoding='utf-8') as f:
            cms_list = json.load(f)
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task, [[target['domain'], _] for _ in cms_list]):
                if future:
                    result_list.append(future)
                sys.stdout.write('\r[{}] Please wait a moment.'.format(['\\', '|', '/', '-'][int(time.time()) % 4]))
        count = len(set(result_list))
        if count == 1:
            return 'web cms', result_list[0]
        elif count == 0:
            return 'web cms', None
        else:
            result_list = ['{}:{:.0%}'.format(_[0], _[1] / count) for _ in Counter(result_list).most_common(count)]
            return 'web cms', ', '.join(result_list)

    def thread_task(self, arg_list):
        try:
            if arg_list[1]['keyword']:
                url = 'http://' + arg_list[0] + arg_list[1]['homeurl']
                response = requests.get(url, timeout=Setting.Options['timeout'])
                content = response.text
                if response.status_code != 200 or content is None:
                    return ''
                if re.search(arg_list[1]['keyword'], content, re.IGNORECASE):
                    result = arg_list[1]['name']
                    return result
            if arg_list[1]['checksum']:
                url = 'http://' + arg_list[0] + arg_list[1]['staticurl']
                response = requests.get(url, timeout=Setting.Options['timeout'])
                content = response.text
                if response.status_code != 200 or content is None:
                    return ''
                md5 = hashlib.md5(content)
                if md5 == arg_list[1]['checksum']:
                    result = arg_list[1]['name']
                    return result
            return ''
        except:
            pass
