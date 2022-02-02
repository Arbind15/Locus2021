from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from authentication.models import userProfile, hospitalProfile
from .models import Chat,ChatBody
import json


def registerNewChat(request):
    try:
        reqBody = json.loads(request.body)
        username = reqBody['username']
        hospital = reqBody['hospital']
        hos_user = User.objects.get(username=hospital)
        usr_user = User.objects.get(username=username)
        chat = Chat.objects.filter(user=usr_user).filter(hospital=hos_user)
        if not chat.exists():
            chat = Chat(user=usr_user, hospital=hos_user)
            chat.save()
            Chat.refresh_from_db(chat)
        return JsonResponse({
            "message": "New Chat Registered!",
            "payload": {}
        }, safe=False)
    except Exception as e:
        return JsonResponse({
            "message": "Something went wrong",
            "payload": {
                "Error": str(e)
            }
        }, safe=False)


def addHospital(request):
    try:
        hos = []
        for h in hospitalProfile.objects.all():
            hos.append(h.username.username)
        return JsonResponse({
            "message": "Hospital List",
            "Hospital": hos
        }, safe=False)
    except Exception as e:
        return JsonResponse({
            "message": "Something went wrong",
            "payload": {
                "Error": str(e)
            }
        }, safe=False)


def chatList(request):
    try:
        reqBody = json.loads(request.body)
        username = reqBody['username']
        usr = User.objects.get(username=username)
        hos = []
        for h in Chat.objects.filter(user=usr):
            hos.append(
                {
                    "Hospital": h.hospital.username,
                    "DateTime": str(h.Date)
                }
            )
        return JsonResponse({
            "message": "Chat List",
            "Hospital": hos
        }, safe=False)
    except Exception as e:
        return JsonResponse({
            "message": "Something went wrong",
            "payload": {
                "Error": str(e)
            }
        }, safe=False)


def chatDetails(request):
    try:
        reqBody = json.loads(request.body)
        username = reqBody['username']
        hospital = reqBody['hospital']
        hos_user = User.objects.get(username=hospital)
        usr_user = User.objects.get(username=username)
        chat=Chat.objects.get(user=usr_user,hospital=hos_user)
        chats = ChatBody.objects.filter(Chat=chat).order_by('pk')
        lst = []
        for chat in chats:
            lst.append({
                "Sender": str(chat.Sender.username),
                "Content": str(chat.Chat_Content),
                "DateTime": str(chat.Date)
            })
        return JsonResponse({
            "message": "Chat details",
            "payload": {
                "chatList": lst
            }
        }, safe=False)

    except Exception as e:
        return JsonResponse({
            "message": "Something went wrong",
            "payload": {
                "Error": str(e)
            }
        }, safe=False)


