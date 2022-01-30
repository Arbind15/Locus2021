from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

def message(req):
    print(req.body)
    return JsonResponse({
        "message": "Message!",
        "payload": {}
    }, safe=False)