#!/bin/bash
cd /var/lib/jenkins/haotian/hao_tian_main
sh stop.sh
sleep 1
nohup python manage.py runserver 0.0.0.0:8010 > server.log 2>&1 &
