'''
任务：

创建一个空列表 students = []。

写一个 for 循环，循环 3 次。

每次循环，让用户输入学生的姓名（name）和成绩（score），并存入一个字典中（如 {"name": name, "score": score}）。

把这个小字典通过 .append() 添加到 students 列表中。

循环结束后，遍历这个 students 列表，打印出所有学生的信息。
'''
students=[]
for i in range(0,3):
    name=input("请输入姓名：")
    score=input("请输入成绩：")
    stu_dict={'name':name,'score':score}
    students.append(stu_dict)
for stu in students:
    print(stu)

'''
•	add_student()：添加学生。
•	show_students()：显示学生。
•	search_student()：查找学生。
'''
def add_student(student_list):
    name=input("please enter your name:")
    score=input("please enter your score:")
    stu_dict={'name':name,'score':score}
    student_list.append(stu_dict)
    print(f"✅ 成功添加学生: {name}")

def show_students(student_list):
    if not student_list: # 如果列表是空的
        print("📭 当前没有任何学生信息。")
        return
    for stu in student_list:
        print(stu)

def search_students(student_list):
    name=input("the name of the student you want to search:")
    for stu in student_list:
        if stu['name']==name:
            print(stu['score'])
            break

    print(f"❌ 未找到名为 {name} 的学生。")

def main():
    my_students = [] # 全局的学生列表
    
if __name__=="__main__":
    main()