from django.contrib.auth.models import User
import json
from django.http import HttpResponse, JsonResponse
from .models import userProfile, hospitalProfile, userStatus, hospitalStatus
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import datetime, date


@csrf_exempt
def registerUser(req):
    if req.method == 'POST':
        reqBody = json.loads(req.body)
        username = reqBody['username']
        password = reqBody['password']
        dob = reqBody['dob']
        ctzn = reqBody['ctzn_id']
        hri = reqBody['hri']

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
            pro = userProfile(username=usr, DOB=dob, Citizenship_Number=ctzn, Health_Stat=hri)
            pro.save()
            userProfile.refresh_from_db(pro)
            stats = userStatus(username=usr)
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


@csrf_exempt
def registerForVaccine(req):
    contex = {}
    reqBody = json.loads(req.body)
    username = reqBody['username']
    add = reqBody['address']
    first_dose = reqBody['first_dose']
    second_dose = reqBody['second_dose']
    cur_pcr = reqBody['cur_pcr']
    try:
        usr = User.objects.get(username=username)
        pre_stats = userStatus.objects.get(username=usr)
        if (first_dose != ""):
            d1 = datetime.strptime(first_dose, "%Y-%m-%d")
            d2 = date.today()
            d2 = datetime.strftime(d2, "%Y-%m-%d")
            d2 = datetime.strptime(d2, "%Y-%m-%d")
            dif = (abs((d2 - d1).days))
            if (dif < 28):
                return JsonResponse({
                    "message": "Minimum days not met!",
                    "payload": {}
                }, safe=False)

        if (pre_stats.New_Vaccine_Request == 1):
            contex['message'] = f"Your vaccination locaction has been changed to: {add}"
        pro = userStatus(usr, New_Vaccine_Location=add, First_Dose_Date=first_dose, Second_Dose_Date=second_dose,
                         Current_PCR=cur_pcr, New_Vaccine_Request=1,Date=datetime.now())
        pro.save()
        hospitalProfile.refresh_from_db(pro)

        if not len(contex) > 0:
            contex['message'] = f"registered for vaccine successfully!"
        contex['payload'] = {}
        return JsonResponse(contex, safe=False)

    except Exception as e:
        return JsonResponse({
            "message": "something_went_wrong",
            "payload": {
                "Error": str(e)
            }
        }, safe=False)


@csrf_exempt
def updateVaccineNumber(req):
    try:
        reqBody = json.loads(req.body)
        hospital_username = reqBody['hos_username']
        user_username = reqBody['user_username']

        usrStat = userStatus.objects.get(username=User.objects.get(username=user_username))
        hosStat = hospitalStatus.objects.get(username=User.objects.get(username=hospital_username))

        if not (hospitalProfile.objects.filter(username=hosStat.username).exists()):
            return JsonResponse({
                "message": "Insufficient Permission",
                "payload": {}
            }, safe=False)

        hosStat.Used_Vaccine = hosStat.Used_Vaccine + 1
        hosStat.save()
        hospitalStatus.refresh_from_db(hosStat)

        if (usrStat.First_Dose_Date == ""):
            usrStat.First_Dose_Date = str(timezone.now())
        if (usrStat.Second_Dose_Date == ""):
            usrStat.Second_Dose_Date = str(timezone.now())
        usrStat.New_Vaccine_Request = 0
        usrStat.New_Vaccine_Location = ""
        usrStat.Schedule_Stat = 0
        usrStat.save()
        userStatus.refresh_from_db(usrStat)

        return JsonResponse({
            "message": "Update successfully!",
            "payload": {}
        }, safe=False)

    except Exception as e:
        return JsonResponse({
            "message": "Something went wrong!",
            "payload": {
                "Error": str(e)
            }
        }, safe=False)
