'''
description: msg_deal
author:zdd
time:2022-09-07
'''
from SW import SW
import goapi
import json


user=SW('202001061028','zd5201314','http://jwgl.sdust.edu.cn/app.do')



user_tips = "欢迎使用记账机器人!功能及使用方法:\n⚡本周账单/统计\n⚡本月账单/统计\n⚡指定月份账单/统计(例如'1月统计')\n⚡指定日期范围账单/统计(例如'指定日期账单@2021-01-23@2021-03-09')\n⚡最近(将查询最近10条交易记录)\n⚡删除(需要先通过最近记录查到pid，如pid为102,则使用'删除 102'\n"
user_tips += "⚡记账功能：回复'名称 金额'即可快捷记账。比如'奶茶 12',中间有空格\n"
user_tips += "\n常见问题FAQ:\n"
user_tips += "1.我的数据存储安全吗？\n答：并不安全，在数据库中使用明文存储。但是，由于qq机器人交互的局限性，菜鸟我当前没有想出合理高效的加密方法，但我承诺不会随意读取数据库中内容。因此，除非遇到设备被盗、黑客攻击，您的账单永远不会被泄露。\n\n"
user_tips += "2.忘记指令怎么办？\n答：回复'帮助'可获得帮助信息。\n\n"
user_tips += "3.统计功能如何分类？\n答：目前机器人只有简单的记账，并不能自动分类。因此，建议您自己约定合适的分类方法，如 就餐、聚餐、学习、零食、美妆、基础物资、电子、生活、娱乐"


def readMsg(user_id,message):
    msg=''
    if '帮助' in message:
        goapi.sendMsg(user_id,user_tips)
    if '本周' in message:
        if '账单' in message:
            msg=getWeekDetail(user_id)
        if '统计' in message:
            pass
    if '本月' in message:
        if '账单' in message:
            msg=getMonthDetail(user_id)
        if '统计' in message:
            pass
    if '课表' in message:
        user.login()
        msg_tmp=''
        msg_kb=json.loads(user.get_class_info())
        print(msg_kb)
        for i in range(0,len(msg_kb)):
            msg_tmp+='第'+str(i+1)+'节课是'+msg_kb[i]['kcmc']+'\n'+'教室是'+msg_kb[i]['jsmc']+'\n'+'时间是'+msg_kb[i]['kssj'] +'-'+msg_kb[i]['jssj']+'\n'
        goapi.sendMsg(user_id,msg_tmp)
    else:
        pass




def getWeekDetail(user_id):
    pass


def getMonthDetail(user_id):
    pass
