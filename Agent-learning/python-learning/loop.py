'''
熟练使用 range() 和 for 循环
知识点： for 循环、range()。
任务：

使用 for 循环和 range()，打印出 1 到 5 的数字（包含 1 和 5）。

使用 for 循环和 range()，打印出 1 到 10 之间所有的偶数。

使用 for 循环和 range()，倒序打印出 5 到 1 的数字（提示：range() 可以传三个参数）。
'''
for i in range(1,6):
    print(i)

for j in range(1,11):
    if j%2==0:
        print(j)

for k in range(5,0,-1):
    print(k)

'''
练习累加与计数（模拟存钱罐）
知识点： 循环的累加（把每次循环的结果加起来）。
任务：
假设你每天往存钱罐里存钱，第一天存 1 元，第二天存 2 元，第三天存 3 元……以此类推。
请写一段代码，计算你 连续存 10 天，存钱罐里总共有多少钱？（提示：需要一个变量在循环外面记录总数，在循环里面不断加上当天的钱）。
'''
total=0
for num in range(1,11):
    total+=num
print(total)

'''
while 循环与 break
知识点： while 循环、break 跳出循环。
任务：
写一个无限循环 while True:，不断让用户输入密码（input()）。

如果用户输入的不是 "888888"，就提示“密码错误，请重试”。

如果用户输入的是 "888888"，打印“密码正确，欢迎登录”，并使用 break 结束循环。
'''
while True:
    password=input()
    if password=="888888":
        print("密码正确，欢迎登录")
        break
    else:
        print("密码错误，请重试")


