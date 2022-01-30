from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from authentication.models import Profile, hospitalProfile

def Temp(req):
    print(req.body)
    # print(Profile.objects.get(pk=2))
    return JsonResponse({
        "message": "Hospital!",
        "payload": {}
    }, safe=False)