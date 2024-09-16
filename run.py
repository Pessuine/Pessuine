from flask import Flask, render_template
from datetime import datetime
import os

# 文件路径定义
visits_file = 'C:\\Users\\Pessuine\\Desktop\\噗云网站\\2024.9.16ver0.0.1\\all_visits.txt'
all_visits = 0

# 检查访问记录文件是否存在，并读取总访问次数
if os.path.exists(visits_file):
    with open(visits_file, 'r') as file:
        all_visits = int(file.read() or 0)

# 创建Flask应用实例
app = Flask(__name__)

# 设置启动日期
setup_date = datetime(2024, 9, 16)

# 主页路由
@app.route('/')
def index():
    global all_visits

    # 访问计数器增加
    all_visits += 1
    # 将新的访问次数写入文件
    with open(visits_file, 'w') as file:
        file.write(str(all_visits))

    # 获取当前时间并计算运行天数
    now = datetime.now()
    already_run_days = (now - setup_date).days + 1

    # 渲染主页模板
    return render_template('index.html', already_run_days=already_run_days, all_visits=all_visits)

# 写作页面路由
@app.route('/writing')
def writing_index():
    global all_visits

    # 获取当前时间并计算运行天数
    now = datetime.now()
    already_run_days = (now - setup_date).days + 1

    # 访问计数器增加
    all_visits += 1
    # 将新的访问次数写入文件
    with open(visits_file, 'w') as file:
        file.write(str(all_visits))

    # 渲染写作页面模板
    return render_template('writing_index.html', already_run_days=already_run_days, all_visits=all_visits)

#小工具页面路由
@app.route('/tools')
def tools_index():
    global all_visits
    # 获取当前时间并计算运行天数
    now = datetime.now()
    already_run_days = (now - setup_date).days + 1

    # 访问计数器增加
    all_visits += 1
    # 将新的访问次数写入文件
    with open(visits_file, 'w') as file:
        file.write(str(all_visits))

    # 渲染小工具页面模板
    return render_template('tools_index.html', already_run_days=already_run_days, all_visits=all_visits)
# 应用启动
if __name__ == '__main__':
    app.run(port="8080")