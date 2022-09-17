# python版本，与虚拟机保持一致
pyenv install 3.8.10 
pyenv global 3.8.10

# 创建和修改db内容
python manage.py makemigrations   demo
python manage.py  migrate   demo