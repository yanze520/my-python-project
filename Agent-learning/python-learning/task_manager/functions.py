import logging
import json
from pathlib import Path
from data_model import Task

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# 获取当前文件（functions.py）所在的绝对路径
BASE_DIR = Path(__file__).resolve().parent
# 把路径和文件名拼起来，生成绝对路径
FILE_NAME = BASE_DIR / "tasks.json"

def load_tasks() -> list:
    #从 JSON 文件加载任务列表
    tasks=[]
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f) # 读出来是字典列表
            for item in data:
                # 将字典重新实例化为 Task 对象
                task = Task(item["task_id"], item["title"], item["status"])
                tasks.append(task)
        logging.info(f"成功加载 {len(tasks)} 个任务。")
    except FileNotFoundError:
        logging.info("未找到历史数据，将创建新文件。")
    except json.JSONDecodeError:
        logging.error("数据文件格式损坏，无法读取！")
    return tasks

def save_tasks(tasks: list) -> None:
    """将任务列表保存到 JSON 文件"""
    # 先利用 to_dict 把对象转成字典，然后再 dump
    data_to_save = [task.to_dict() for task in tasks]
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        # ensure_ascii=False 保证中文正常显示，indent=4 让文件排版好看
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)

def add_tasks(tasks: list):
    title = input("请输入任务内容: ")
    # 自动生成 ID：如果有任务，就取最大 ID + 1，否则从 1 开始
    if tasks:
        new_id = max(task.task_id for task in tasks) + 1
    else:
        new_id = 1
    
    new_task = Task(new_id, title)
    tasks.append(new_task)
    save_tasks(tasks) # 写完立刻保存
    logging.info(f"成功添加任务：{title}")

def view_tasks(tasks: list):
    if not tasks:
        print("当前没有任务，快去添加吧！")
        return
    
    print("\n--- 任务列表 ---")
    for task in tasks:
        status_icon = "✅" if task.status == "done" else "⭕"
        print(f"{task.task_id}. {status_icon} {task.title}")
    print("----------------\n")


def complete_task(tasks: list):
    view_tasks(tasks) # 先展示一下，方便用户看 ID
    if not tasks: return
    
    try:
        task_id = int(input("请输入要完成的任务 ID: "))
    except ValueError:
        print("输入无效，请输入数字 ID！")
        return

    for task in tasks:
        if task.task_id == task_id:
            task.status = "done" # 修改状态
            save_tasks(tasks)    # 保存
            logging.info(f"任务 {task_id} 已完成。")
            print("任务状态已更新！")
            return
    print("未找到该 ID 的任务。")

def delete_task(tasks: list):
    view_tasks(tasks)
    if not tasks: return
    
    try:
        task_id = int(input("请输入要删除的任务 ID: "))
    except ValueError:
        print("输入无效，请输入数字 ID！")
        return

    # 重新生成一个不包含该 ID 的列表
    for i, task in enumerate(tasks):
        if task.task_id == task_id:
            del tasks[i]         # 从列表中删除
            save_tasks(tasks)    # 保存
            logging.info(f"任务 {task_id} 已删除。")
            print("任务已删除！")
            return
    print("未找到该 ID 的任务。")