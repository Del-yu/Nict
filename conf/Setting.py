# -*-* coding:UTF-8 -*-*

""" 如无必要，请勿修改配置信息 """
# 程序的版本
VERSION = '3.0'

# HTTP请求头配置
DEFAULT_HTTP_HEADERS = {
    'Accept': "*/*",
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Connection': 'close'}

# 扫描端口对应服务配置
DEFAULT_PORT_SERVICES = {
    '21': 'FTP',
    '22': 'SSH',
    '23': 'Telnet',
    '25': 'SMTP',
    '53': 'DNS',
    '67': 'DHCP',
    '68': 'DHCP',
    '69': 'TFTP',
    '80': 'HTTP',
    '109': 'POP3',
    '110': 'POP3',
    '137': 'NetBIOS',
    '139': 'NetBIOS',
    '143': 'IMAP',
    '161': 'SNMP',
    '389': 'LDAP',
    '443': 'HTTPS',
    '445': 'SMB',
    '465': 'SMTPS',
    '489': 'LDAP',
    '512': 'Linux R RPE',
    '513': 'Linux R RLT',
    '514': 'Linux R cmd',
    '873': 'Rsync',
    '993': 'IMAPS',
    '995': 'POP3',
    '1080': 'Proxy',
    '1090': 'JavaRMI',
    '1098': 'JavaRMI',
    '1099': 'JavaRMI',
    '1158': 'Oracle EMCTL',
    '1352': 'Lotus',
    '1433': 'MSSQL',
    '1434': 'MSSQL Monitor',
    '1521': 'Oracle',
    '1723': 'PPTP',
    '1873': 'Rsync',
    '2082': 'cPanel admin panel/CentOS web panel',
    '2083': 'CPanel admin panel/CentOS web panel',
    '2100': 'Oracle XDB FTP',
    '2181': 'Zookeeper',
    '2222': 'DA admin panel',
    '2375': 'Docker',
    '2601': 'Zebra',
    '2604': 'Zebra',
    '3000': 'Gitea Web',
    '3128': 'Squid Proxy',
    '3306': 'MySQL',
    '3311': 'Kangle admin panel',
    '3312': 'Kangle admin panel',
    '3389': 'RDP',
    '3690': 'SVN',
    '4440': 'Rundeck',
    '4848': 'GlassFish',
    '5000': 'SysBase/DB2',
    '5432': 'PostgreSql',
    '5632': 'PcAnywhere',
    '5800': 'VNC',
    '5900': 'VNC',
    '5938': 'TeamViewer',
    '5984': 'CouchDB',
    '6082': 'varnish',
    '6379': 'Redis',
    '6380': 'Redis',
    '6800': 'Aria2',
    '7001': 'Weblogic',
    '7002': 'Weblogic',
    '7778': 'Kloxo admin panel',
    '8069': 'Zabbix',
    '8161': 'ActiveMQ',
    '8291': 'RouterOS/Winbox',
    '8080': 'Web',
    '9001': 'Weblogic',
    '9043': 'WebSphere',
    '9060': 'WebSphere',
    '9080': 'WebSphere',
    '9090': 'WebSphere',
    '9200': 'Elasticsearch',
    '9300': 'Elasticsearch',
    '10000': 'Virtualmin/Webmin',
    '10050': 'Zabbix agent',
    '10051': 'Zabbix server',
    '10990': 'JavaRMI',
    '11211': 'Memcached',
    '14147': 'FileZilla Manager',
    '27017': 'MongoDB',
    '27018': 'MongoDB',
    '50000': 'SAP NetWeaver',
    '50030': 'Hadoop',
    '50050': 'CobaltStrike',
    '50070': 'Hadoop',
    '61616': 'ActiveMQ',
    '62078': 'iPhone-sync',
}

# CMS识别字典配置
DEFAULT_CMS_DICT = 'Cms.json'

# 中间件识别字典配置
DEFAULT_MID_DICT = 'Mid.json'

# 不启用插件名单配置 'DisArea', 'DisCdn', 'DisPort', 'DisSub'
DEFAULT_PLUGIN_OFF = ['']

# 参数存储变量定义
global Options

# 插件储存列表定义
global DiscoverPlugins
global AuxiliaryPlugins

# 收集的信息存储列表定义
global Information
