#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
import datetime
while 1:
    def reserce():
        global kecheng
        if w == 0:
            return "9:35 3—4—114 通信原理 "
        elif w == 1:
            return "9:35 5—6—215 电子线路设计 \r\n\r\n 2:00 7-8-107 微机原理 \r\n\r\n 19:00 5-6-309 文献信息检索"
        elif w == 2:
            return "7:50 7-8-405 微机原理 \r\n\r\n 10:30  3-4-102 通信原理"
        elif w == 3:
            return "9:35 7-8-407 通信电子线路 \r\n\r\n 2:00 3-4-108 语音信号处理 "
        elif w == 4:
            return "9:35 7-8-403 嵌入式系统与应用 "
        elif w == 5:
            return "周六快乐"
        elif w == 6:
            return "周日快乐"
    my_sender='746355941@qq.com'    
    my_pass = 'halknuapgrfcbeba'            
    my_user='zyjs7463@qq.com'    
    def mail():
        ret=True
        try:
            msg=MIMEText(kecheng,'plain','utf-8')
            msg['From']=formataddr(["FromRunoob",my_sender])  
            msg['To']=formataddr(["FK",my_user])             
            msg['Subject']="嘀嘀嘀"              
     
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)  
            server.login(my_sender, my_pass)  
            server.sendmail(my_sender,[my_user,],msg.as_string())  
            server.quit()  
        except Exception:  
            ret=False
        return ret
    now = datetime.datetime.now()
    w = datetime.datetime.today().weekday()
    if now.hour ==5 and now.minute == 30:
        kecheng = reserce()
        ret=mail()
    time.sleep(59)

