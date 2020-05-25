#微博系统的安装和使用

#安装相关的包
pip install -r requirements.txt

#设置环境变量
#mac
export FLASK_MODE=default
#Windows
set FLASK_MODE=default

#本地运行
python manage.py runserver
#可以在http://127.0.0.1:5000/查看系统

#服务器上运行
python3 manage.py runserver --host='0.0.0.0' --port=8080
#可以使用服务器IP:端口号来访问系统