'''
descrpition:  api for go-cq
author:zdd
time:2022-09-22
'''
#coding = utf-8
import requests


def sendMsg(user_id,msg):
    url='http://127.0.0.1:5700/send_private_msg'
    data = {'user_id': user_id, 'message': msg}
    res=requests.post(url=url,params=data)
    print(f"回复用户@{user_id}：{msg[:20]}")
    return res.text





def add_request(request_flag):
    url = 'http://127.0.0.1:5801/set_friend_add_request'
    data = {'flag':str(request_flag)}
    res = requests.get(url,params=data)
    print("加好友成功")
    return res.text


