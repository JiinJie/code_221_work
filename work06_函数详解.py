# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 11:25
# @Author  : jinjie

# 1、编写函数f_1 ，使其可以根据输入的参数，返回指定数量的“*”

def f_1(n):
    print("*"*n)

# 2、编写函数f_2，使其可以根据参数决定调用f_1的次数 默认为一次
def f_2(n=1):
    for i in range(n):
        f_1(n)

if __name__ == '__main__':
    # f_1(1)
    # f_1(3)

    f_2(3)