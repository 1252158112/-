import json
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import END
import tkinter as tk
import main
import time
from threading import Timer
def login():
    username=user.get()
    password=psw.get()
    tp=main.login(username,password)
    print(tp)
    try:
        if ('错' in tp or '未' in tp):
            var.set(tp)
    except BaseException:
        var.set('登录成功')
        global s
        s=tp

def getMySeat() :
    global s
    ret=main.getMySeat(s)
    logmes = ''
    for one in ret:
        logmes+=one['timeDesc']+'--'+one['labName']+'--'+one['roomName']+'--'+one['devName']+'\n'
    log.insert(END, logmes)
    log.see(END)
def mkTimer():
    nh = int(time.strftime("%H", time.localtime()))
    nm = int(time.strftime("%M", time.localtime()))
    ns = int(time.strftime("%S", time.localtime()))
    ntot=nh*60*60+nm*60+ns
    npre=22*60*60+29*60+30
    if ntot>=npre:
        npre+=24*60*60
    logmes='定时'+str(npre-ntot)+'s成功\n'
    log.insert(END, logmes)
    log.see(END)
    Timer(npre - ntot - 10, login, ()).start()
    Timer(npre - ntot, quickGetSeat, ()).start()
def quickGetSeat():
    global s,qtime,qmid
    date=  qdate.get()
    dateRange = qdateRange.get()
    kind_id = quick_id[qkind_id.current()]
    interval = qinterval.get()
    tm=1

    try:
        logmes=''
        for tm in range(1,int(qtime.get())+1):
            ret=main.quickGetSeat(s,date,dateRange,kind_id,interval)
            logmes+=str(tm) +'-->'+ret[1] +'-->'+time.strftime("%M:%S", time.localtime()) +'\n'
            if(ret[0]==1):
                logmes += '成功预约'+'\n'
                break
            else:
                time.sleep(float(qmid.get()))
        log.insert(END, logmes)
        log.see(END)
    except BaseException:
        log.insert(END, '尚未登录或失去网络链接'+'\n')


def addLog(root):
    global log
    log = scrolledtext.ScrolledText(root, width=70, height=13,font=('宋体',10) )  # 滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
    log.pack()  # 滚动文本框在页面的位置
    return root

def packLogin(root):
    logFrame=tk.Frame(MFrame)
    logFrame.pack(side='left')
    global var
    var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
    l = tk.Label(logFrame, textvariable=var)
    l.pack()
    global user,psw
    l1 = tk.Label(logFrame, text='账号')
    l2 = tk.Label(logFrame, text='密码')
    user = tk.Entry(logFrame)
    psw = tk.Entry(logFrame)
    l1.pack()
    user.pack()
    l2.pack()
    psw.pack()
    log=tk.Button(logFrame, text='登录', command=login)
    check = tk.Button(logFrame, text='查询预约', command=getMySeat)
    check.pack(side='bottom')
    log.pack(side='bottom')
    return root
def packGetSeat(qgetSeatFrameroot):
    qgetSeatLabelFrame = tk.Frame(MFrame)
    qgetSeatLabelFrame.pack(side='left')
    qgetSeatFrame = tk.Frame(MFrame)
    qgetSeatFrame.pack(side='right')
    ndate=tk.StringVar(value=time.strftime("%Y-%m-%d", time.localtime()))
    # print(ndate)
    global qdate, qdateRange, qkind_id, qinterval,qtime,qmid
    qdate = tk.Entry(qgetSeatFrame,textvariable=ndate)
    ndaterange=tk.StringVar(value='07:00-22:00')
    qdateRange = tk.Entry(qgetSeatFrame,textvariable=ndaterange)
    number=tk.StringVar
    qkind_id = ttk.Combobox(qgetSeatFrame,textvariable=number,width=17)
    qkind_id['value']=('北区自习室','电子阅览室','南区自习室')
    ninterval = tk.StringVar(value='120')
    qinterval = tk.Entry(qgetSeatFrame,textvariable=ninterval)
    ntime = tk.StringVar(value='500')
    qtime = tk.Entry(qgetSeatFrame, textvariable=ntime)
    nmid = tk.StringVar(value='0.1')
    qmid = tk.Entry(qgetSeatFrame, textvariable=nmid)
    # tk.Label(qgetSeatFrame, text='快速占座').pack()
    tk.Label(qgetSeatLabelFrame,text='预约日期:').pack()
    qdate.pack()
    tk.Label(qgetSeatLabelFrame, text='预约时间:').pack()
    qdateRange.pack()
    tk.Label(qgetSeatLabelFrame, text='预约自习室位置:').pack()
    qkind_id.pack()
    tk.Label(qgetSeatLabelFrame, text='预约自习持续(min):').pack()
    qinterval.pack()
    tk.Label(qgetSeatLabelFrame, text='争抢次数:').pack()
    qtime.pack()
    tk.Label(qgetSeatLabelFrame, text='争抢间隔(s):').pack()
    qmid.pack()
    qgetSeat = tk.Button(qgetSeatFrame, text='快速抢座', command=quickGetSeat)
    qgetSeat.pack()
    makeTm = tk.Button(qgetSeatLabelFrame, text='定时抢座', command=mkTimer)
    makeTm.pack()
    return root
def drawTh(root):
    root.title('图书馆工具')
    root.geometry('500x500')
    root = addLog(root)
    root = packLogin(root)
    root = packGetSeat(root)
    return root
if __name__== '__main__':

    global username,password
    global s,roomList,seatList
    global MFrame
    roomList = main.initRoom()
    seatList = main.initSeat()
    quick_id = ['100531888', '1005335015', '105364879']  # 北区自习室，电子阅览室，南区自习室id
    root=tk.Tk()
    MFrame=tk.Frame(root)
    MFrame.pack()
    root=drawTh(root)

    root.mainloop()