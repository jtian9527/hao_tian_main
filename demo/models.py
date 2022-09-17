# -*- coding: utf-8 -*-
from django.db import models


class Demo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    creator = models.CharField(max_length=50)
    ctime = models.PositiveIntegerField()
    mtime = models.PositiveIntegerField()
    is_delete = models.SmallIntegerField()

if __name__ == '__main__':
    pass
