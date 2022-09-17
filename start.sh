#!/bin/bash
ps -aux | grep python | grep 8010 | grep -v grep  | awk '{print $2}' | xargs kill -9
sleep 2
nohup python manage.py runserver 0.0.0.0:8010 > server.log 2>&1 &
