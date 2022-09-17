#!/bin/bash
sleep 2
nohup python manage.py runserver 0.0.0.0:8010 > server.log 2>&1 &
