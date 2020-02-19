# encoding: utf-8
"""
@author: 程序员小小叶
@contact: 3203636266@qq.com
@微信公众号：程序员小小叶
@time: 2020/2/19 11:57
@file: case1.py
@desc: 
"""
from wxpy import *

bot = Bot(cache_path=True) # 模拟登陆

wifi_boss = bot.search('小可爱')[0]  # 这里‘’填入微信昵称
print(wifi_boss)


@bot.register()  # 接收从指定好友发来的消息，发送者即recv_msg.sender为指定好友wifi_boss
def recv_send_msg(recv_msg):
	print('收到的消息：', recv_msg.text)  # recv_msg.text取得文本
	if recv_msg.sender == wifi_boss:
		recv_msg.forward(bot.file_helper, prefix='老婆留言: ')  # 在文件传输助手里留一份，方便自己忙完了回头查看
		ms = '老婆最美丽，我对老婆的爱如滔滔江水，连绵不绝'
		print('>>>给老婆回复的：', ms)
		return ms  # 给老婆回一份


# 进入Python命令行，让程序保持运行
embed()
