# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 8:59
# @Author  : jinjie

# 1、输出10以内被3整除的整数
def calculate():
    for i in range(10):
        if i%3 == 0 :
            print(i)
        else:
            continue

# 2、切换字符串字母大小写
a = "We Will Rock You"
def change_letters(a):
    a = list(a)
    b=[]
    for n in a:
        if "a" <= n <= "z":
            b.append(n.upper())
        elif"A" <= n <= "Z":
            b.append(n.lower())
        else:
            b.append(n)
    print("".join(b))

if __name__ == '__main__':
    calculate()
    print("-" * 50)
    change_letters(a)


    print("-" * 50)
# 2、修改版

def swapcase_letters(letter):
    b = letter.swapcase()
    print(b)

swapcase_letters(a)




