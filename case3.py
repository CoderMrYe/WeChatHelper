# encoding: utf-8
"""
@author: 程序员小小叶
@contact: 3203636266@qq.com
@微信公众号：程序员小小叶
@time: 2020/2/19 12:39
@file: case3.py
@desc: 
"""
import time
from wxpy import *
from threading import Thread

bot = Bot(cache_path=True)

client_baba = bot.search('小可爱')[0]  # 这里‘’填入微信客户昵称
print(client_baba)

'''
设定一个定时发送线程
'''
def timer(target, ok_time):
	while (True):
		now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
		print(now_time)
		if ok_time == now_time:
			# 发送文本
			# client_baba.send('Hello, WeChat!')
			# 发送图片
			# client_baba.send_image('Test.png')
			# 发送视频
			# client_baba.send_video('Test.mov')
			# 发送文件
			target.send_file('Test.zip')
			# 以动态的方式发送图片
			# client_baba.send('@img@Test.png')


t = Thread(target=timer, args=(client_baba, '2020-02-19 13:33:11',))
t.start()
