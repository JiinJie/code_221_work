# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 10:40
# @Author  : jinjie

# 1、编写代码打印以下效果

line = 5
j = 1
for i in range(line):
    print("*"*j)
    j += 2


# 2、打印9*9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}X{j}={i*j}\t",end='')
    if i == j:
        print("")   # 为什么print("\n")会自动换两行呢，不加判断时却不会换行


