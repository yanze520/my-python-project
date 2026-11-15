'''
认识 def 和基础参数
知识点： 定义函数、传递参数。
任务：

定义一个函数 greet(name)，接收一个名字作为参数。

在函数内部，打印 "你好, [name]!"。

调用这个函数，分别传入你自己的名字和一个朋友的名字。
'''
def greet(name):
    print(f'你好，{name}!')

greet("zhangsan")

'''
理解 return 与 print 的区别
知识点： 返回值。
任务：

定义一个函数 add_numbers(a, b)，计算 a + b 的结果，并用 return 返回这个结果（不要在函数里 print）。

在函数外面，调用这个函数，把返回的结果存到一个变量 result 里。

打印 result 并乘以 2。
'''
def add_numbers(a,b):
    return a+b
result=add_numbers(1,2)
print(result*2)

'''
默认参数
知识点： 默认参数。
任务：

定义一个函数 order_coffee(type="拿铁", size="中杯")。

函数内部打印 f"为您制作：{size} {type}"。

尝试用三种方式调用它：

不传任何参数。

只传 type="美式"。

传入 type="卡布奇诺", size="大杯"。
'''

def order_coffee(type='拿铁',size='中杯'):
    print(f'为您制作：{size}{type}')

order_coffee()
order_coffee(type="美式")
order_coffee(type="美式",size="大杯")

'''
定义一个函数 add_student(students_list)，接收一个列表作为参数。

在函数内部，用 input() 让用户输入姓名和成绩。

将输入的信息组装成字典 {"name": name, "score": score}，并 append 到传入的 students_list 中。

注意： 这个函数不需要 return 列表，因为列表是可变对象，在函数内部修改它，外部的列表也会跟着变（这就是传递引用的特性）。

在主程序里，创建一个空列表 my_students = []，调用 add_student(my_students)，然后打印 my_students 看看数据有没有成功加进去。
'''
def add_student(student_list):
    name=input("please enter your name:")
    score=input("please enter your score:")
    stu_dict={'name':name,'score':score}
    student_list.append(stu_dict)
my_students=[]
add_student(my_students)
print(my_students)
