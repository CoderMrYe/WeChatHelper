# encoding: utf-8
"""
@author: 程序员小小叶
@contact: 3203636266@qq.com
@微信公众号：程序员小小叶
@time: 2020/2/19 12:29
@file: case2.py
@desc: 
"""
from wxpy import *

bot = Bot(cache_path=True)

lover_group = bot.groups().search('群名字')[0]  # 第一步找到群名字

lover = lover_group.search('女神')[0]  # 第二步在群里找到女神名字


@bot.register(chats=lover_group)  # 接收从指定群发来的消息，发送者即recv_msg.sender为组
def recv_send_msg(recv_msg):
	print('收到的消息：', recv_msg.text)
	if recv_msg.member == lover:
		# 这里不用recv_msg.render 因为render是群的名字
		recv_msg.forward(bot.file_helper, prefix='女神发言: ')
		return '女神大人沉鱼落雁，闭月羞花'


# 进入Python命令行，让程序保持运行
embed()
