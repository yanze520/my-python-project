#专门放类的定义
class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def show_info(self):
        print(f'学生：{self.name}，成绩：{self.score}')
