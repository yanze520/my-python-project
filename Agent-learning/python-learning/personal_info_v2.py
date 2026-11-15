'''
名字（str）

年龄（int）

身高（float）
然后输出类似：“你好，[名字]！你明年就 [年龄+1] 岁了，你的身高是 [身高] 米。”
'''
name=input("请输入你的名字")
age=input("请输入你的年龄")
height=input("请输入你的身高（米）")
print(f'你好，{name}！你明年就{int(age)+1}岁了，你的身高是{height}米')