#!/bin/bash
cd /var/lib/jenkins/haotian/hao_tian_main

sh stop.sh
sleep 1
nohup python manage.py runserver 0.0.0.0:8010 > server.log 2>&1 &
sleep 1
# 检查进程是否正常启动
pid_count=`ps -aux | grep python | grep 8010 | grep -v grep  | wc -l `
if [ 0 == $pid_count ];then
  echo "python 8010 pid no exit"
  exit 1
fi
