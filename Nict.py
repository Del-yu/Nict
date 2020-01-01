# -*-* coding:UTF-8
import importlib
import os
import re
import sys
import click
import traceback
from conf import Setting
from lib.banner import Banner
from lib.style.ColorPrint import ColorPrint
from lib.core.CollectInfo import CollectInfo


def check_target(ctx, param, value):
    try:
        # 检查输入内容是否正确
        if re.match('^[\w\.]*\.[\w]+$', value):
            return value
        else:
            raise click.BadParameter('Format is incorrect')
    except:
        raise click.BadParameter('Error target')


def list_plugins(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    # 列出插件目录下所有插件
    plugins = [os.listdir(os.path.join('plugins', 'discover', 'lowlevel')),
                               os.listdir(os.path.join('plugins', 'discover', 'midlevel')),
                               os.listdir(os.path.join('plugins', 'discover', 'highlevel'))]
    if len(plugins) == 0:
        ColorPrint('No plugin list', 'error')
    index = 0
    print('\nList all plugins:\n')
    for _id, level in enumerate(plugins):
        for plugin_name in level:
            if not plugin_name.endswith(".py") or plugin_name.startswith("_"):
                continue
            index += 1
            plugins_obj = importlib.import_module('plugins.discover.{}.{}'.format(
                ['lowlevel', 'midlevel', 'highlevel'][_id], plugin_name[:-3]))
            print('\t{}:\t名称:{}\t简介:{}'.format(index, plugin_name[:-3], plugins_obj.DiscoverModule().description))
    ctx.exit()


def show_version(ctx, param, value):
    # 显示程序版本
    if not value or ctx.resilient_parsing:
        return
    click.echo('Current version {}'.format(Setting.VERSION))
    ctx.exit()


@click.command()
@click.option('--target', help='设置信息收集的目标.', callback=check_target)
@click.option('--plugin', help='设置运行加载的插件.')
@click.option('--plugin-list', help='列出所有可用的插件.', is_flag=True, callback=list_plugins, expose_value=False, is_eager=True)
@click.option('--force', help='强制进行子域名检测.', is_flag=True)
@click.option('--level', help='设置信息搜集的级别, 默认2.', type=click.IntRange(1, 3), default=2)
@click.option('--process', help='设置运行进程的数量, 默认4.', type=click.IntRange(1, 60), default=4)
@click.option('--threads', help='设置运行线程的数量, 默认80.', type=click.IntRange(1, 999), default=80)
@click.option('--timeout', help='设置超时连接的时间, 默认10秒.', default=10)
@click.option('--nocolor', help='关闭颜色打印的功能.', is_flag=True)
@click.option('--output', help='输出结果到指定文件.')
@click.option('--version', help='显示当前程序的版本.', is_flag=True, callback=show_version, expose_value=False, is_eager=True)
def cli(**kwargs):
    """Easy to use internet information collection tool"""
    os.system("")
    Setting.Options = kwargs
    return main()


def main():
    # 程序的主函数
    Banner.show()
    check_environment()
    CollectInfo().start_up()


def check_environment():
    # 检查当前运行环境、解释器版本是否适合运行
    ColorPrint('Check the current environment', 'info')
    if sys.version_info[0] < 3:
        ColorPrint("Must be using Python 3.x", 'error')
    try:
        # 检查导入的模块是否被安装
        import dns
        import click
        import requests
        import tldextract
        import prettytable
    except:
        exec_msg = traceback.format_exc()
        if any(_ in exec_msg for _ in ("ImportError", "ModuleNotFoundError", "Can't find file for module")):
            ColorPrint("Invalid runtime environment : %s" % exec_msg.split("Error: ")[-1].strip(), 'error')
        raise SystemExit


if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        pass
    except SystemExit:
        raise
