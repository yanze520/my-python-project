'''
编码 & 标识符
知识点：标识符命名规则（字母/下划线开头，区分大小写，不能用关键字）。
题目：定义几个变量来存储一本书的信息，要求变量名符合规范且能看出含义：
书名（如 "Python入门"）
作者名（如 "张三"）
出版年份（如 2024）
是否绝版（布尔值，如 False）
最后用 print 把这些信息打印出来。
'''
book="Python入门"
author="zhangsan"
year=2024
out_of_print=False
print(book,author,year,out_of_print)

'''
多行语句
知识点：用反斜杠 \ 或括号 ()、[]、{} 来写多行语句。
题目：有三个数字 1、2、3，要求用多行语句的形式（至少用一次反斜杠 \）把它们相加，并打印结果。
'''
total=1+\
      2+\
      3
print(sum)

'''
数字(Number)类型 & 字符串(String)
知识点：int、float、bool、complex 类型；字符串的拼接、重复、切片。
题目：
定义变量 a = 123，b = 3.14，c = True，d = 1 + 2j，分别打印它们的值。
定义一个字符串 s = "Python"，打印：
字符串的长度
第一个字符和最后一个字符
字符串反转（用切片 [::-1]）
字符串重复3次
'''

a=123
b=3.14
c=True
d=1+2j
print(a)
print(b)
print(c)
print(d)
s="Python"
print(len(s))
print(s[0],s[-1])
print(s[::-1])
print(s*3)

'''
等待用户输入
知识点：input() 函数。
题目：让用户输入姓名和年龄，然后打印一句“你好，[姓名]！你今年[年龄]岁了。”
'''
name=input("your name:")
age=input("your age")
print(name+age)


'''
同一行显示多条语句
知识点：用分号 ; 分隔多条语句。
题目：在同一行里，定义变量 x = 10，y = 20，然后打印 x + y 的结果。
'''
x=10;y=20
print(x+y)

'''
print 输出（换行与不换行）
知识点：print() 默认换行，end="" 可以不换行。
题目：用 print 输出 "Hello" 和 "World"：

第一次让它们分两行显示

第二次让它们在同一行显示（中间用空格隔开）
'''
print("hello")
print("world")

print("hello",end=" ")
print("world")

'''
import 与 from...import
知识点：导入模块的几种方式。
题目：

用 import math 导入数学模块，计算并打印 16 的平方根。

用 from math import pi 导入圆周率，打印 pi 的值。
'''
import math
from math import pi

print(math.sqrt(16))
print(pi)

'''
命令行参数（可选挑战）
知识点：sys.argv 获取命令行参数。
题目：写一个脚本，打印出运行脚本时传入的所有命令行参数。比如运行 python script.py hello world，输出应包含 hello 和 world。
'''
import sys
print(sys.argv)