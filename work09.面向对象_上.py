# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 8:52
# @Author  : jinjie

import time

class Date(Year,Month,Day):
    # year = year
    # month = month
    # day = day


    def show(self):
        now_time = time.localtime(time.time())
        print("当前日期：{}",now_time)
    print("{}年{}月{}日".format(year,month,day))

if __name__ == '__main__':
    data1 = Date(2022,11,11)
    # print(data1)
