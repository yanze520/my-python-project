代码片段

VSCode 允许创建自定义代码片段，提高编写重复性代码的效率。打开命令面板（快捷键Ctrl+Shift+P 、Cmd+Shift+P ），输入 “Configure User Snippets”，选择或创建一个新的代码片段文件。例如，创建一个 Python 中定义函数的代码片段，在代码片段文件中添加如下内容：

"Python function": {

"prefix": "def_func",

"body": [

"def $1($2):",

" $3"

],

"description": "Define a Python function"

}

这样，在编写 Python 代码时，输入 “def_func” 并触发智能提示，就会出现定义函数的代码模板，只需根据需要填写函数名、参数和函数体即可。