from functions import *

def main():
    tasks = load_tasks() # 程序启动时先加载数据
    while True:
        print("\n===== 任务管理系统 =====")
        print("1. 查看任务")
        print("2. 添加任务")
        print("3. 完成任务")
        print("4. 删除任务")
        print("5. 退出")

        choice = input("请选择: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("再见！")
            break
        else:
            print("无效选项！")

if __name__ == "__main__":
    main()