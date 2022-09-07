#coding=utf-8
from flask import Flask,request
import goapi
import randomdsa
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



if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5701',debug=False)
