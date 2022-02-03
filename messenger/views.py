from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from authentication.models import userProfile, hospitalProfile
from .models import Chat, ChatBody
import json
from django.db.models import Q


@csrf_exempt
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


@csrf_exempt
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


@csrf_exempt
def chatList(request):
    print(request.body)
    try:
        reqBody = json.loads(request.body)
        username = reqBody['username']
        flag=reqBody['flag']
        usr = User.objects.get(username=username)
        hos = []
        if int(flag)==0:
            for h in Chat.objects.filter(user=usr).order_by('-pk'):
                hos.append(
                    {
                        "User": h.hospital.username,
                        "DateTime": str(h.Date)
                    }
                )
        else:
            for h in Chat.objects.filter(hospital=usr).order_by('-pk'):
                hos.append(
                    {
                        "User": h.user.username,
                        "DateTime": str(h.Date)
                    }
                )
        return JsonResponse({
            "message": "Chat List",
            "Users": hos
        }, safe=False)
    except Exception as e:
        return JsonResponse({
            "message": "Something went wrong",
            "payload": {
                "Error": str(e)
            }
        }, safe=False)


@csrf_exempt
def chatDetails(request):
    print(request.body)
    try:
        reqBody = json.loads(request.body)
        username = reqBody['username']
        hospital = reqBody['hospital']
        flag = reqBody['flag']
        hos_user = User.objects.get(username=hospital)
        usr_user = User.objects.get(username=username)
        # if int(flag)==0:
        #     hos_user = User.objects.get(username=hospital)
        #     usr_user = User.objects.get(username=username)
        # else:
        #     hos_user = User.objects.get(username=username)
        #     usr_user = User.objects.get(username=hospital)
        print(usr_user)
        print(hos_user)
        chat = Chat.objects.filter(user=usr_user).filter(hospital=hos_user)
        if not chat.exists():
            chat = Chat(user=usr_user, hospital=hos_user)
            chat.save()
            Chat.refresh_from_db(chat)

        chat = Chat.objects.get(user=usr_user, hospital=hos_user)
        print(chat)
        chats = ChatBody.objects.filter(Chat=chat).order_by('pk')
        lst = []
        for chat in chats:
            lst.append({
                "Sender": str(chat.Sender.username),
                "Content": str(chat.Chat_Content),
                "DateTime": str(chat.Date)
            })

        # chat = Chat.objects.filter(Q(user=usr_user) | Q(hospital=hos_user))
        # if int(flag) != 1:
        #     chat = Chat.objects.filter(user=usr_user, hospital=hos_user)
        #     if not chat.exists():
        #         chat = Chat(user=usr_user, hospital=hos_user)
        #         chat.save()
        #         Chat.refresh_from_db(chat)
        #
        #     chat = Chat.objects.get(user=usr_user, hospital=hos_user)
        #     print(chat)
        #     chats = ChatBody.objects.filter(Chat=chat).order_by('pk')
        #     lst = []
        #     for chat in chats:
        #         lst.append({
        #             "Sender": str(chat.Sender.username),
        #             "Content": str(chat.Chat_Content),
        #             "DateTime": str(chat.Date)
        #         })
        # else:
        #     chat = Chat.objects.filter(user=hos_user, hospital=usr_user)
        #     if not chat.exists():
        #         chat = Chat(user=hos_user, hospital=usr_user)
        #         chat.save()
        #         Chat.refresh_from_db(chat)
        #
        #     chat = Chat.objects.get(user=hos_user, hospital=usr_user)
        #     print(chat)
        #     chats = ChatBody.objects.filter(Chat=chat).order_by('pk')
        #     lst = []
        #     for chat in chats:
        #         lst.append({
        #             "Sender": str(chat.Sender.username),
        #             "Content": str(chat.Chat_Content),
        #             "DateTime": str(chat.Date)
        #         })

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



@csrf_exempt
def getModeList(request):
    try:
        hos=[]
        users=[]
        for usr in userProfile.objects.all():
            users.append(str(usr.username.username))
        for hospital in hospitalProfile.objects.all():
            hos.append(str(hospital.username.username))
        return JsonResponse({
            "message": "Mode List",
            "payload": {
                "users": users,
                "hospitals":hos
            }
        }, safe=False)
    except Exception as e:
        return JsonResponse({
            "message": "Cannot load list",
            "payload": {
                "Error": str(e)
            }
        }, safe=False)