# -*-* coding:UTF-8
import re
import sys
import requests
import tldextract
from conf import Setting
from lib.core.ClassObject import Discover
from lib.style.ColorPrint import ColorPrint


class DiscoverModule(Discover):
    def __init__(self):
        super().__init__()
        self.description = '收集与目标站点相关子域名'

    def start_up(self, target):
        # 去掉域名前缀
        one_domain = tldextract.extract(target['domain']).domain + '.' + tldextract.extract(target['domain']).suffix
        sys.stdout.write('\r[-] Please wait a moment.')
        subdomains = list(set(self.simple_task(one_domain)))
        if target['domain'] in subdomains:
            subdomains.remove(target['domain'])
        if subdomains:
            return 'subdomains', subdomains
        else:
            return 'subdomains', None

    def simple_task(self, arg):
        subdomains_list = []
        try:
            search_url = 'https://site.ip138.com/{}/domain.htm'.format(arg)
            response = requests.get(search_url, headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            search_result = re.findall('<a.*target="_blank">(.*\.' + arg + ')</a>', response.text)
            for _ in search_result:
                subdomains_list.append(_ + '.' + arg)
        except:
            ColorPrint('IP138 search subdomains failure', 'warn')
        try:
            search_url = 'https://securitytrails.com/domain/{}/dns'.format(arg)
            response = requests.get(search_url, headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            search_result = re.findall('"subdomains":(.*?),"stats"', response.text)[0]
            for _ in eval(search_result):
                subdomains_list.append(_ + '.' + arg)
        except:
            ColorPrint('Securitytrails search subdomains failure', 'warn')
        return subdomains_list
