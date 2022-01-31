from django.contrib.auth.models import User
import json
from django.http import HttpResponse, JsonResponse
from .models import userProfile, hospitalProfile,userStatus
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def registerUser(req):
    if req.method == 'POST':
        reqBody = json.loads(req.body)
        username = reqBody['username']
        password = reqBody['password']
        dob = reqBody['dob']
        ctzn = reqBody['ctzn_id']

        if (User.objects.filter(username=username).exists()):
            return JsonResponse({
                "message": "username_already_exists",
                "payload": {}
            }, safe=False)

        if (userProfile.objects.filter(Citizenship_Number=ctzn).exists()):
            return JsonResponse({
                "message": "citizenship_num_already_exists",
                "payload": {}
            }, safe=False)

        try:
            usr = User.objects.create_user(username=username, email='', password=password)
            pro = userProfile(username=usr, DOB=dob, Citizenship_Number=ctzn)
            pro.save()
            userProfile.refresh_from_db(pro)
            stats=userStatus(username=usr)
            stats.save()
            userStatus.refresh_from_db(stats)

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

    return JsonResponse({
        "message": "forbidden",
        "payload": {}
    }, safe=False)

@csrf_exempt
def loginUser(req):
    if req.method == 'POST':
        reqBody = json.loads(req.body)
        username = reqBody['username']
        password = reqBody['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if not (userProfile.objects.filter(username=user).exists()):
                return JsonResponse({
                    "message": "Insufficient Permission",
                    "payload": {}
                }, safe=False)

            login(req, user)

            pro = userProfile.objects.get(username=user)

            return JsonResponse({
                "message": "logged_in",
                "payload": {
                    "username": user.username,
                    "dob": pro.DOB,
                    "ctzn_id": pro.Citizenship_Number
                }
            }, safe=False)

        else:
            return JsonResponse({
                "message": "username_does_not_exists",
                "payload": {}
            }, safe=False)
    return JsonResponse({
        "message": "forbidden",
        "payload": {}
    }, safe=False)

@csrf_exempt
def getUserInfo(req):
    print(req.body)
    reqBody = json.loads(req.body)
    print(reqBody)
    return JsonResponse({
        "message": "user_info",
        "payload": {}
    }, safe=False)

@csrf_exempt
def registerHospital(req):
    reqBody = json.loads(req.body)
    username = reqBody['username']
    password = reqBody['password']
    phone = reqBody['phone']
    add = reqBody['address']

    if (User.objects.filter(username=username).exists()):
        return JsonResponse({
            "message": "username_already_exists",
            "payload": {}
        }, safe=False)

    try:
        usr = User.objects.create_user(username=username, email='', password=password)
        pro = hospitalProfile(username=usr, Phone_Number=phone, Address=add)
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

@csrf_exempt
def loginHospital(req):
    reqBody = json.loads(req.body)
    username = reqBody['username']
    password = reqBody['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if not (hospitalProfile.objects.filter(username=user).exists()):
            return JsonResponse({
                "message": "Insufficient Permission",
                "payload": {}
            }, safe=False)

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

@csrf_exempt
def getHospitalInfo(req):
    print(req.body)
    reqBody = json.loads(req.body)
    print(reqBody)
    return JsonResponse({
        "message": "user_info",
        "payload": {}
    }, safe=False)
