# -*- coding: utf-8 -*-
from demo.models import *
from django.forms import model_to_dict
import time
import json
from django.http import JsonResponse

def list(request):
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    demo_list = Demo.objects.filter(is_delete=0)
    result_list = []
    for demo in demo_list:
        demo = model_to_dict(demo)
        result_list.append(demo)
    return JsonResponse(result_list,safe=False)


def create_demo(request):
    body = json.loads(request.body)
    name = body.get("name", "who")
    now_time = int(time.time())
    demo_param = Demo(
        name=name,
        creator="hao.tian",
        is_delete=0,
        ctime=now_time,
        mtime=now_time,
    )
    demo_param.save()
    demo_id = demo_param.id
    return JsonResponse(demo_id,safe=False)
