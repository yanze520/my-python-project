#专门放处理逻辑的函数
from models import Student

def add_student(students_list):
    name = input("请输入姓名: ")
    score = input("请输入成绩: ")
    # 注意：这里不再是建字典了，而是实例化一个 Student 对象！
    new_student = Student(name, score)
    students_list.append(new_student)
    print("添加成功！")

def show_students(students_list):
    for stu in students_list:
        # 注意：这里调用对象的方法，而不是打印字典
        stu.show_info()
