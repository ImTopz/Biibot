#coding=utf-8
from flask import Flask,request
import goapi
import click
import random
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
        else:
            goapi.sendMsg(user_id,"抱歉,您不是好友,无法使用此功能")


    elif(data.get('post_type')=='request'):
        pass



    else:
        pass

    return 'OK'


@click.command()
@click.option('--host', default='localhost', help='set hostname to listen on')
@click.option('--port', default=5000, help='set service port')
@click.option('--debug', default=False, help='set debug symbol')
def main(host, port, debug):
    """Accounting bot based on gocq-http and flask"""
    app.run(host, port, debug)

if __name__ == '__main__':
    main()
