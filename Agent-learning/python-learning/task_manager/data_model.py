class Task:
    def __init__(self,task_id:int, title:str, status:str="todo"):
        self.task_id = task_id
        self.title = title
        self.status = status

    # 把对象转成字典，方便后续存成 JSON
    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "status": self.status
        }
    