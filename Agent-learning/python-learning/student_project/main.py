from manager import add_student, show_students # 导入函数

def main():
    my_students = []
    while True:
        print("\n1. 添加学生\n2. 显示学生\n3. 退出")
        choice = input("请选择: ")
    
        if choice == '1':
            add_student(my_students)
        elif choice == '2':
            show_students(my_students)
        elif choice == '3':
            print("再见！")
            break

if __name__ == "__main__":
    main()