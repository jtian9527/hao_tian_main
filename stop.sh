ps -aux | grep python | grep 8010 | grep -v grep  | awk '{print $2}' | xargs kill -9