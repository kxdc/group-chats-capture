import itchat
from time import time, ctime
from datetime import date
from itchat.content import *
from pathlib import Path


@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO],
                     isGroupChat=True)
def information(msg):

    # collect following field of received group char message
    msg_group_name = msg['User']['NickName']
    msg_from_uname = msg['FromUserName']
    msg_nickname = msg['ActualNickName']
    msg_content = msg['Content']
    msg_create_time = msg['CreateTime']
    msg_type = msg['Type']

    single_msg = '[{gname}] [{nname}] [{rtime}] [{mtype}] "{mcontent}" [{fname}]\n'.format(
        gname=msg_group_name,
        nname=msg_nickname,
        rtime=ctime(msg_create_time),
        mtype=msg_type,
        mcontent=msg_content,
        fname=msg_from_uname)
    print(single_msg)

    # save the txt file with the name of group name
    # locate the txt file in a path named by date
    filename = pathname + '/' + msg_group_name + '.txt'
    pathname = date.today().strftime("%b-%d-%Y")
    Path(pathname).mkdir(parents=True, exist_ok=True)
    with open(filename, 'a') as writer:
        writer.write(single_msg)


def after_login():

    chat_rooms = itchat.search_chatrooms(name=target_group_name)

    if len(chat_rooms) > 0:
        print('[{stime}]: found group chat "{gname}"'.format(
            stime=ctime(time()), gname=target_group_name))
    else:
        print('[{stime}]: not found group chat "{gname}" !!!'.format(
            stime=ctime(time()), gname=target_group_name))
        exit(1)


def after_exit():
    print("exit !!")


if __name__ == '__main__':

    filename = ''
    target_group_name = ''  # check whether the group is found
    itchat.auto_login(enableCmdQR=2,
                      hotReload=True,
                      loginCallback=after_login,
                      exitCallback=after_exit)

    itchat.run()
