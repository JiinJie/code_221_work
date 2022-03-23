# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 8:45
# @Author  : jinjie

# 1、有列表 l = [2,3,4,5,1]，编写代码，移除列表中小于3的数字
l = [2,3,4,5,1]

for i in l:
    if i < 3:
        l.remove(i)
print(l)

print("-" * 50)

# 2、有字符串a = "abbaccadd"，编写代码，分析a出现的次数
a = "abbaccadd"
find_count= a.count("a")
print("a出现的次数为：{} 次".format(find_count))

print("-" * 50)

# 3、有字符串a = "abbaccadd"，编写代码，分析字符串由哪些字母组成
a = "abbaccadd"
set_a = set(a)
print(f"字符串a由 {set_a} 组成")