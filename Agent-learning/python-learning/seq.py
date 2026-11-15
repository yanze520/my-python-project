'''
列表的“增删改查” (List)
知识点： 列表的基础操作。
任务：

创建一个列表 fruits = ["苹果", "香蕉", "橘子"]。

增：在末尾添加“西瓜”。

改：把列表里的“香蕉”改成“芒果”。

删：删除“橘子”。

查：打印出列表的长度，并把最终修改好的列表打印出来。
'''
fruits = ["苹果", "香蕉", "橘子"]
fruits.append("西瓜")
fruits[1]="芒果"
fruits.remove("橘子")
print(len(fruits))
print(fruits)
'''
元组与集合的特点 (Tuple & Set)
知识点： 元组不可变、集合去重。
任务：

创建一个元组 point = (10, 20)。尝试用 point[0] = 15 修改它，看看会报什么错（直接在代码里注释掉错误的那行即可）。

创建一个包含重复数字的列表 nums = [1, 2, 2, 3, 3, 3, 4]，利用集合 set() 将其去重，然后转回列表并打印。
'''
point = (10, 20)
point[0] = 15
nums = [1, 2, 2, 3, 3, 3, 4]
nums_set=set(nums)
new_nums=list(nums_set)
print(new_nums)
'''
字典的“增删改查” (Dict)
知识点： 字典的键值对操作。
任务：

创建一个字典 student = {"name": "张三", "age": 20}。

增：添加一个键值对 "score": 95。

改：把年龄改为 21 岁。

删：删除 "age" 这个键值对（可以用 del 或 .pop()）。

查：通过键获取学生的名字，并打印。
'''
student = {"name": "张三", "age": 20}
student["score"]=95
student["age"]=21
del student["age"]
print(student["name"])

'''
用 for 循环遍历 (List & Dict)
知识点： 遍历列表和字典。
任务：

用 for 循环遍历列表 movies = ["肖申克的救赎", "阿甘正传", "泰坦尼克号"]，打印出每个电影名字。如果嫌麻烦，可以加上序号（如 1. 肖申克的救赎）。

用 for 循环遍历字典 phone = {"品牌": "苹果", "型号": "iPhone 15", "价格": 5999}，打印出类似 品牌: 苹果 的格式。（提示：遍历字典时用 .items() 最佳）。
'''
movies = ["肖申克的救赎", "阿甘正传", "泰坦尼克号"]
for movie in movies:
    print(movie)

phone = {"品牌": "苹果", "型号": "iPhone 15", "价格": 5999}
for key,value in phone.items:
    print(f'{key}:{value}')

'''
理解“嵌套” (Nested)
知识点： 嵌套列表、嵌套字典。
任务：

创建一个嵌套列表 matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]，打印出里面的数字 5。

创建一个嵌套字典（类似大作业里的结构）：
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
class_info = {
    "student_1": {"name": "张三", "age": 20, "score": 90},
    "student_2": {"name": "李四", "age": 21, "score": 85}
}
print(matrix[1][1])
print(class_info["student_2"]["score"])