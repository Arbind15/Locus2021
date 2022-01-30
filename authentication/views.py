from django.contrib.auth.models import User
import json
from django.http import HttpResponse, JsonResponse
from .models import Profile, hospitalProfile
from django.contrib.auth import login, authenticate, logout


def registerUser(req):
    reqBody = json.loads(req.body)
    username = reqBody['username']
    password = reqBody['password']
    email = reqBody['email']
    phone = reqBody['phone']
    dob = reqBody['dob']
    add = reqBody['address']

    if (User.objects.filter(username=username).exists()):
        return JsonResponse({
            "message": "username_already_exists",
            "payload": {}
        }, safe=False)

    if (User.objects.filter(email=email).exists()):
        return JsonResponse({
            "message": "email_already_exists",
            "payload": {}
        }, safe=False)

    try:
        usr = User.objects.create_user(username=username, email=email, password=password)
        pro = Profile(username=usr, Phone_Number=phone, Address=add, DOB=dob)
        pro.save()
        Profile.refresh_from_db(pro)

        return JsonResponse({
            "message": "profile_saved",
            "payload": {}
        }, safe=False)

    except Exception as e:
        return JsonResponse({
            "message": "something_went_wrong",
            "payload": {
                "Error": str(e)
            }
        }, safe=False)


def loginUser(req):
    reqBody = json.loads(req.body)
    username = reqBody['username']
    password = reqBody['password']

    user = authenticate(username=username, password=password)

    if not (Profile.objects.filter(username=user).exists()):
        return JsonResponse({
            "message": "Insufficient Permission",
            "payload": {}
        }, safe=False)

    if user is not None:
        login(req, user)
        return JsonResponse({
            "message": "logged_in",
            "payload": {}
        }, safe=False)

    else:
        return JsonResponse({
            "message": "username_does_not_exists",
            "payload": {}
        }, safe=False)


def getUserInfo(req):
    print(req.body)
    reqBody = json.loads(req.body)
    print(reqBody)
    return JsonResponse({
        "message": "user_info",
        "payload": {}
    }, safe=False)


def registerHospital(req):
    reqBody = json.loads(req.body)
    username = reqBody['username']
    password = reqBody['password']
    email = reqBody['email']
    phone = reqBody['phone']
    estd = reqBody['estd']
    add = reqBody['address']
    pan = reqBody['pan']

    if (User.objects.filter(username=username).exists()):
        return JsonResponse({
            "message": "username_already_exists",
            "payload": {}
        }, safe=False)

    if (User.objects.filter(email=email).exists()):
        return JsonResponse({
            "message": "email_already_exists",
            "payload": {}
        }, safe=False)

    try:
        usr = User.objects.create_user(username=username, email=email, password=password)
        pro = hospitalProfile(username=usr, Phone_Number=phone, Address=add, ESTD=estd, Pan_Number=pan)
        pro.save()
        hospitalProfile.refresh_from_db(pro)

        return JsonResponse({
            "message": "profile_saved",
            "payload": {}
        }, safe=False)

    except Exception as e:
        return JsonResponse({
            "message": "something_went_wrong",
            "payload": {
                "Error": str(e)
            }
        }, safe=False)


def loginHospital(req):
    reqBody = json.loads(req.body)
    username = reqBody['username']
    password = reqBody['password']

    user = authenticate(username=username, password=password)

    if not (hospitalProfile.objects.filter(username=user).exists()):
        return JsonResponse({
            "message": "Insufficient Permission",
            "payload": {}
        }, safe=False)

    if user is not None:
        login(req, user)
        return JsonResponse({
            "message": "logged_in",
            "payload": {}
        }, safe=False)

    else:
        return JsonResponse({
            "message": "username_does_not_exists",
            "payload": {}
        }, safe=False)


def getHospitalInfo(req):
    print(req.body)
    reqBody = json.loads(req.body)
    print(reqBody)
    return JsonResponse({
        "message": "user_info",
        "payload": {}
    }, safe=False)
