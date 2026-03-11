# from pywechat.utils import auto_reply_to_group_decorator
#
#
# @auto_reply_to_group_decorator(duration='2min', group_name='测试消息', at_only=True, at_other=False, close_wechat=False)
# def reply_func(newMessage):
#     print(newMessage)
#     if '你好' in newMessage:
#         return '你好,请问有什么可以帮您的吗?'
#     if '在吗' in newMessage:
#         return '在的,请问有什么可以帮您的吗?'
#     if '售后' in newMessage:
#         return '''您好，您可以点击下方链接申请售后:
#         https://github.com/Hello-Mr-Crab/pywechat'''
#     if '算了' in newMessage or '不需要了' in newMessage:
#         return '不好意思.未能为您提供满意的服务,欢迎下次光临'
#     return '不好意思，未能理解您的需求'  # 最后总是要返回一个值，不要出现newMessage不在列举的情况,返回None
#
#
# reply_func()
from wxauto import WeChat
from wxauto.msgs import FriendMessage
import time

wx = WeChat()

# 消息处理函数
def on_message(msg, chat):
    # 示例1：将消息记录到本地文件
    # with open('msgs.txt', 'a', encoding='utf-8') as f:
    #     f.write(msg.content + '\n')
    #
    # # 示例2：自动下载图片和视频
    # if msg.type in ('image', 'video'):
    #     print(msg.download())
    print(msg,chat)
    # 示例3：自动回复收到
    if isinstance(msg, FriendMessage):
        msg.quote('收到')

    ...# 其他处理逻辑，配合Message类的各种方法，可以实现各种功能
# wx.SendMsg(msg="你好", who="测试消息", clear=True, at="", exact=False)
# 添加监听，监听到的消息用on_message函数进行处理
wr=wx.AddListenChat(nickname="测试消息", callback=on_message)
print(wr)
wx.StartListening()
# 保持程序运行
wx.KeepRunning()