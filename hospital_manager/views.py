from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from authentication.models import userProfile, hospitalProfile, adminProfile,hospitalStatus
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import math
import json, os, datetime
from covidResponse.settings import MEDIA_ROOT
from scheduler.views import  scheduler
from django.http import FileResponse
from .dailyReportGenerator import generatePDF


def CalculateInfectionRate(initial_infect, final_infect):
    d = {}
    for lbl1, num1, lbl2, num2 in zip(initial_infect.keys(), initial_infect.values(), final_infect.keys(),
                                      final_infect.values()):
        diff = num2 - num1
        if diff < 0:
            diff = 0
        d[lbl1] = diff
    return d

def CalculateDistributeVaccine(infectionRate, finale, totalVaccine, rateParm, ratioParm):
    d = {}
    assigned_vaccine = {}

    final_sum = 0
    for lbl, num1, num2 in zip(infectionRate.keys(), infectionRate.values(), finale.values()):
        nn = num1 * rateParm + num2 * ratioParm
        final_sum += nn
        d[lbl] = nn

    for lbl, num in zip(d.keys(), d.values()):
        ratio = num / final_sum
        d[lbl] = ratio
        assigned_vaccine[lbl] = math.floor(ratio * totalVaccine)

    return assigned_vaccine

def Temp(req):
    print(req.body)
    # print(Profile.objects.get(pk=2))
    return JsonResponse({
        "message": "Hospital!",
        "payload": {}
    }, safe=False)


def Login(request):
    contex = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if not (adminProfile.objects.filter(username=user).exists()):
                if not user.is_staff == True:
                    messages.error(request, f'Insufficient Permission!')
                    return render(request, 'hospital_manager/login.html')

            login(request, user)

            return redirect('home')

        else:
            messages.error(request, f'Username does not exists!')
            return render(request, 'hospital_manager/login.html')

    return render(request, 'hospital_manager/login.html', contex)


@login_required(login_url='login')
def Home(request):
    contex = {}
    if request.method=='POST':
        return generatePDF()
    return render(request, 'hospital_manager/home.html', contex)


@login_required(login_url='login')
def DistributVaccine(request):
    contex = {}
    vac_code = request.POST.get('vac_code')
    vac_num = int(request.POST.get('vac_num'))
    rate_parm = float(request.POST.get('rate_parm'))
    ratio_parm = float(request.POST.get('ratio_parm'))

    data_loc = os.path.join(MEDIA_ROOT, 'data')

    with open(data_loc + '/initialInfPop.json', 'r') as openfile:
        # Reading from json file
        initial = json.load(openfile)

    with open(data_loc + '/finalInfPop.json', 'r') as openfile:
        # Reading from json file
        finanal = json.load(openfile)

    inf_rate = CalculateInfectionRate(initial, finanal)
    assigned_vac = CalculateDistributeVaccine(inf_rate, finanal, vac_num, rate_parm,
                                              ratio_parm)
    contex['assigned_vaccs'] = zip(assigned_vac.keys(), initial.values(), finanal.values(), inf_rate.values(),
                                   assigned_vac.values())
    return render(request, 'hospital_manager/vacc_assigned_list.html', contex)


@login_required(login_url='login')
def AssigneVaccine(request):
    contex = {}
    try:
        vac_code = request.POST.get('vac_code')
        vac_num = int(request.POST.get('vac_num'))
        rate_parm = float(request.POST.get('rate_parm'))
        ratio_parm = float(request.POST.get('ratio_parm'))

        data_loc = os.path.join(MEDIA_ROOT, 'data')

        with open(data_loc + '/initialInfPop.json', 'r') as openfile:
            # Reading from json file
            initial = json.load(openfile)

        with open(data_loc + '/finalInfPop.json', 'r') as openfile:
            # Reading from json file
            finanal = json.load(openfile)

        inf_rate = CalculateInfectionRate(initial, finanal)
        assigned_vac = CalculateDistributeVaccine(inf_rate, finanal, vac_num, rate_parm,
                                                  ratio_parm)

        json_object = json.dumps(assigned_vac, indent=4)
        with open(data_loc + "/ass(" + str(datetime.datetime.now()).replace(':', '-') + ").json", "w") as outfile:
            outfile.write(json_object)

        for lbl, num in zip(assigned_vac.keys(),assigned_vac.values()):
            stats=hospitalStatus(username=User.objects.get(username=lbl),Vaccine_Code=vac_code,Total_Assigned_Vaccine=num)
            stats.save()
            hospitalStatus.refresh_from_db(stats)

        # with open(data_loc+'/vacc_codes.json', 'r+') as file:
        #     file_data = json.load(file)
        #     file_data[vac_code]=''
        #     file.seek(0)
        #     json.dump(file_data, file, indent=4)

        return redirect('schedule')
    except Exception as e:
        contex['mssg'] = f"Something went wrong while Assigning vaccine to hospitals ({e})"
        return render(request, 'hospital_manager/message_div.html', contex)



@login_required(login_url='login')
def SendDistibuteDiv(request):
    contex = {}
    return render(request, 'hospital_manager/distributeDiv.html', contex)


@login_required(login_url='login')
def SendQueueDiv(request):
    contex = {}

    if request.method == 'POST':
        per_old = request.POST.get('per')
        date = request.POST.get('date')
        data_loc = os.path.join(MEDIA_ROOT, 'data')
        json_object = json.dumps({"old percentage": per_old, "date": date}, indent=4)
        with open(data_loc + "/QueuingParms.json", "w") as outfile:
            outfile.write(json_object)

        contex['mssg'] = "Parameter Updated!!"

        return render(request, 'hospital_manager/message_div.html', contex)

    return render(request, 'hospital_manager/queueDiv.html', contex)


@login_required(login_url='login')
def ViewUsers(request):
    contex = {}
    users_pro = userProfile.objects.all()
    contex['profiles'] = enumerate(users_pro, start=1)
    return render(request, 'hospital_manager/userList.html', contex)


@login_required(login_url='login')
def ViewHospitals(request):
    contex = {}
    pro = hospitalProfile.objects.all()
    contex['profiles'] = enumerate(pro, start=1)
    return render(request, 'hospital_manager/hospitalList.html', contex)


@login_required(login_url='login')
def registerHospitalFromFile(request):
    contex = {}
    data_loc = os.path.join(MEDIA_ROOT, 'data')
    with open(data_loc + '/initialInfPop.json', 'r') as openfile:
        qParms = json.load(openfile)

    # print(qParms.keys())
    for lbl in qParms.keys():
        try:
            if not (User.objects.filter(username=lbl).exists()):
                usr = User.objects.create_user(username=lbl, email='', password=str(lbl + '@123'))
                pro = hospitalProfile(username=usr, Address=lbl)
                pro.save()
                hospitalProfile.refresh_from_db(pro)
        except:
            pass
    contex['mssg'] = "Registration Done from District List!!!"
    return render(request, 'hospital_manager/message_div.html', contex)


@login_required(login_url='login')
def generateDailyReport(request):
    contex = {}
    return FileResponse(open(MEDIA_ROOT+'/default.jpg','rb'),filename='default.jpg',as_attachment=True)