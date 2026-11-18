'''
知识点： pip 安装、虚拟环境。
任务：

打开 VS Code 的终端，确保你的虚拟环境 (.venv) 是激活的。

在终端里输入：pip install requests 安装一个非常有名的第三方库。

在代码里 import requests，并尝试请求一个网页，打印它的状态码：
response = requests.get("https://www.baidu.com")
print(response.status_code)
(注：如果你看到输出 200，说明你的网络请求成功了！)
'''

import requests
response = requests.get("https://www.baidu.com")
print(response.status_code)

'''
初识类与对象
知识点： class 定义、实例化对象。
任务：

定义一个最简单的类 Dog，里面用 pass 占位。

用这个类实例化两只小狗：dog1 = Dog() 和 dog2 = Dog()。

用 print(type(dog1)) 看看它是什么类型。
'''
class Dog:
    pass
dog1=Dog()
dog2=Dog()
print(type(dog1))

'''
__init__() 和 self
知识点： 类的初始化方法、实例属性。
任务：

定义一个类 Book。

编写 __init__(self, title, author) 方法，让它在创建对象时，把 title 和 author 绑定到 self 上。

实例化一本书：my_book = Book("Python入门", "张三")。

打印出这本书的 title 和 author。
'''
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
my_book=Book("python-learning","zhansgan")
print(my_book.title,my_book.author)

'''
知识点： 在类中定义函数、使用 self。
任务：

定义一个类 Student。

在 __init__(self, name, score) 里接收姓名和成绩，并绑定到 self。

定义一个方法 show_info(self)，在这个方法里面打印 f"学生：{self.name}，成绩：{self.score}"。

创建一个学生对象 stu1 = Student("李四", 95)，并调用它的 show_info() 方法。
'''
class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def show_info(self):
        print(f'学生：{self.name}，成绩：{self.score}')

stu1=Student("lisi",95)
stu1.show_info()