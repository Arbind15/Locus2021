import random

from django.shortcuts import render
import json, os
from django.http import HttpResponse, JsonResponse
from authentication.models import userProfile, hospitalProfile, adminProfile, hospitalStatus, userStatus
from datetime import datetime, date, timedelta
from covidResponse.settings import MEDIA_ROOT
from django.views.decorators.csrf import csrf_exempt

# from hospital_manager.fileHandler import districts
data_loc = os.path.join(MEDIA_ROOT, 'data')

with open(data_loc + '/QueuingParms.json', 'r') as openfile:
    qParms = json.load(openfile)

old_per = qParms['old percentage']
vac_date = qParms['date']

priority_1 = []
priority_0 = []
to_be_vaccinated = []


class dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


def priority_assigner(jsn_fil):
    dob = jsn_fil['dob']
    health_status = jsn_fil['health_stats']
    identifier = jsn_fil['id']
    d1 = datetime.strptime(dob, "%Y-%m-%d")
    d2 = date.today()
    d2 = datetime.strftime(d2, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    age = (abs((d2 - d1).days)) / 365
    if age > 60 or health_status == 1:
        priority_1.append(identifier)
    else:
        priority_0.append(identifier)


def queue_generator(percent_of_hri, available_no_vaccine):
    global to_be_vaccinated
    registered_hri = len(priority_1)
    max_num_of_hri = int((percent_of_hri / 100) * available_no_vaccine)
    if registered_hri<max_num_of_hri:
        no_of_hri=registered_hri
    else:
        no_of_hri=max_num_of_hri
    no_of_general = available_no_vaccine - no_of_hri
    to_be_vaccinated = priority_1[:no_of_hri] + priority_0[:no_of_general]


def scheduler(vaccination_date, users_parms, percent_of_hri, available_no_vaccine,
              hospital_username):
    for parm in users_parms:
        priority_assigner({'dob': parm['dob'], 'health_stats': parm['health_stats'], 'id': parm['id']})
    queue_generator(percent_of_hri, available_no_vaccine)
    scheduled_dict = dictionary()
    initial_dt = vaccination_date + ' ' + '10:00:00'
    initial_dt = datetime.strptime(initial_dt, "%Y-%m-%d %H:%M:%S")
    new_dt = initial_dt
    tc = 0
    for identifier in to_be_vaccinated:
        scheduled_dict.key = identifier
        scheduled_dict.value = str(new_dt)
        scheduled_dict.add(scheduled_dict.key, scheduled_dict.value)
        tc += 1
        if tc > 3:
            time_change = timedelta(minutes=5)
            new_dt = initial_dt + time_change
            tc = 0
            test_dt = new_dt.strftime("%H:%M:%S")
            if int(test_dt[:2]) == 16:
                time_change = timedelta(hours=18, minutes=5)
                new_dt = initial_dt + time_change
    # print(scheduled_dict)
    json_object = json.dumps(scheduled_dict, indent=4)
    data_loc = os.path.join(MEDIA_ROOT, 'data')
    with open(data_loc + '/vaccine_Schedule/' + str(hospital_username) + '.json', "w") as outfile:
        outfile.write(json_object)
    json_object=None
    return scheduled_dict


# print(scheduler("2045-04-03", "2005-04-03",1,5,10,1230))
@csrf_exempt
def schedule(req):
    contex={}
    global priority_0,priority_1,to_be_vaccinated
    try:
        hospitals = hospitalProfile.objects.all()
        for hospital in hospitals:
            user_parms = []
            users = userStatus.objects.filter(New_Vaccine_Location=hospital.Address).filter(
                New_Vaccine_Request=1)
            for user in users:
                user_parms.append({
                    'dob': str(user.username.userprofile.DOB),
                    'health_stats': int(user.username.userprofile.Health_Stat),
                    'id': user.username.username,
                })
            # print(user_parms)

            scheduler(vac_date, user_parms, float(old_per),
                      hospitalStatus.objects.get(username=hospital.username).Total_Assigned_Vaccine,
                      hospital.username.username)
            to_be_vaccinated = []
            priority_0 = []
            priority_1 = []

    except Exception as e:
        contex['mssg'] = f"Something went wrong while scheduling vaccine({e})"
        return render(req, 'hospital_manager/message_div.html', contex)

    contex['mssg'] = "Vaccine Assigned and Scheduled!!!"
    return render(req, 'hospital_manager/message_div.html', contex)
