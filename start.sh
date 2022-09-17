#!/bin/bash
ps -aux | grep python | grep 8010 | grep -v grep  | awk '{print $2}' | xargs kill -9
echo "stop 8010"
sleep 2
echo "start 8010"
nohup python manage.py runserver 0.0.0.0:8010 > server.log 2>&1 &
echo "finish 8010"
