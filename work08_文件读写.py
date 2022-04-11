# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 9:37
# @Author  : jinjie
import datetime
import dateutil
import time

# 1. 编写一个copy函数，接收2个参数（源路径、目标路径），可以实现文件的拷贝
def copy(source_path,target_path):
    fread = open(source_path,'rb')
    fwrite = open(target_path,'wb')

    while True:
        data = fread.read(1024)
        if not data:
            break
        fwrite.write(data)
        # print("复制成功")

    fread.close()
    fwrite.close()


copy(r"D:\\caiji_system_report",r"D:\\caiji_system_report_copy")


#  2. 编写一个函数，计算当前，距离10.1国庆，还差几天
def calculate_national():
    now_time = time.localtime(time.time())
    date_year_now = datetime.datetime.now().year
    date_month_now = datetime.datetime.now().month

    if date_month_now < 10:
        date_str = str(date_year_now) + "-10-01"
    else:
        date_str = str(date_year_now+1) + "-10-01"

    date_national = time.strptime(date_str,"%Y-%m-%d")

    date1 = datetime.datetime(date_national[0],date_national[1],date_national[2])
    date2 = datetime.datetime(now_time[0],now_time[1],now_time[2])
    diff_days = (date1-date2).days
    return diff_days

if __name__ == '__main__':
    print(f"还有{calculate_national()}天是下一个国庆节")
