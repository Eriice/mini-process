# -*-coding:utf-8 -*-
import multiprocessing
 
# 监听本机的5000端口
bind = '0.0.0.0:5000'
 
preload_app = True
 
# 开启进程
# workers=4
workers = multiprocessing.cpu_count() * 2 + 1
 
# # 每个进程的开启线程
threads = multiprocessing.cpu_count() * 2
 
backlog = 2048
 
# #工作模式为meinheld
# # worker_class = "egg:meinheld#gunicorn_worker"
 
debug=True
 
# # 如果不使用supervisord之类的进程管理工具可以是进程成为守护进程，否则会出问题
# daemon = True
 
# 日志级别 
loglevel = 'debug'
# 进程pid记录文件
pidfile = 'logs/pid.log'
logfile = 'logs/debug.log'
accesslog = 'logs/access.log'

access_log_format = '%(h)s %(t)s %(U)s %(q)s'
