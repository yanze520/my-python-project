'''
知识点： 捕获异常。
任务：

让用户输入一个数字，并尝试把它转换成整数 int()。

如果用户输入了字母（比如 "abc"），会引发 ValueError。

使用 try...except ValueError: 来捕获它，并打印：“输入错误，请输入纯数字！”
'''
num=input("please enter a number:")
try:
    num_int=int(num)
except ValueError:
    print("输入错误，请输入纯数字！")
else:
    print(f"转换成功，你输入的数字是{num_int}")
finally:
    print("程序执行完毕")

'''
知识点： open() 和 with open()。
任务：

使用 with open("test.txt", "w", encoding="utf-8") as f: 打开一个文件（w 表示写入，encoding 防止中文乱码）。

使用 f.write() 往里面写入两行内容：
"Python 是一门很棒的语言。"
"我正在学习文件操作。"

去 VS Code 左侧的文件管理器里，点开刚刚生成的 test.txt 看看内容。
'''
with open("text.txt","w",encoding="utf-8") as f:
    f.write("Python 是一门很棒的语言。\n")
    f.write("我正在学习文件操作。")

'''
知识点： 读取文件内容。
任务：

使用 with open("test.txt", "r", encoding="utf-8") as f: 打开你刚刚写的文件（r 表示只读）。

使用 f.read() 读取全部内容，并打印出来。

（进阶）使用 f.readlines() 读取所有行，存成一个列表，然后用 for 循环打印每一行。
'''