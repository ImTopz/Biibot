'''
descripe:main for Biibot
author:zdd
time:2022-09-07
'''

#coding=utf-8
from flask import Flask,request
import goapi
import time
import random
import msgRead


num=0

app=Flask(__name__)

@app.route('/',methods=['POST'])
def getEvent():
    data=request.json
    if(data.get('post_type')=='message'):
        message_type=data.get('message_type')
        msg=data.get('message')
        user_id=data.get('user_id')
        if(message_type=='private'):
            print(f"接收消息@{user_id}:{msg[:20]}")
            msgRead.readMsg(user_id,msg)

        else:
            goapi.sendMsg(user_id,"抱歉,您不是好友,无法使用此功能")


    elif(data.get('post_type')=='request'):
        global num
        num=num+1
        request_type=data.get('request_type')
        if(request_type=='friend'and num==1):
            user_id = str(data.get('user_id'))
            comment = str(data.get('comment'))
            flag = str(data.get('flag'))
            print(f"接收加好友请求@{user_id}:{comment[:20]}")
            time.sleep(random.randint(2, 5))
            goapi.add_request(flag)
            time.sleep(random.randint(4, 10))
            goapi.sendMsg(user_id, msgRead.user_tips)
            num=0 # 防止多次发送初始化消息




    else:
        pass

    return data



if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5701',debug=False)
