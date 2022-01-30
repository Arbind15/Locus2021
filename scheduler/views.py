from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime, date, timedelta

priority_1 = []
priority_0 = []
to_be_vaccinated = []


def lineSchedule(req):
    print(req.body)
    return JsonResponse({
        "message": "Line ma baas bhai, sabai ko palo aauxa!",
        "payload": {}
    }, safe=False)


class dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


def priority_assigner(age, health_status, identifier):
    if age > 60 or health_status is 1:
        priority_1.append(identifier)
    else:
        priority_0.append(identifier)


def per_def(user_clearance):
    if user_clearance == "L1":
        percent_of_hri = input("Enter the percentage of old and high risk individuals")
    else:
        raise Exception("Forbidden")
    return percent_of_hri


def queue_generator(percent_of_hri, available_no_vaccine):
    total_registered = len(priority_1) + len(priority_0)
    no_of_hri = int((percent_of_hri / 100) * total_registered)
    no_of_general = available_no_vaccine - no_of_hri
    to_be_vaccinated = priority_1[:no_of_hri] + priority_0[:no_of_general]
    return to_be_vaccinated


def security_check(last_vaccine_date, covid_status):
    d1 = date.today()
    d1 = d1.strftime("%Y-%m-%d")
    d2 = last_vaccine_date
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    difference = abs((d2 - d1).days)
    if difference >= 28 and covid_status is False:
        return "Passed"
    else:
        return "Failed"


def covid_status(last_report, report_date):
    if last_report is True:
        d1 = date.today()
        d1 = d1.strftime("%Y-%m-%d")
        d2 = report_date
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        difference = abs((d2 - d1).days)
        if difference > 30:
            return False
        else:
            return True
    else:
        return False


def scheduler(to_be_vaccinated, vaccination_date):
    scheduled_dict = dictionary()
    initial_dt = vaccination_date + ' ' + '10:00:00'
    initial_dt = datetime.strptime(initial_dt, "%Y-%m-%d %H:%M:%S")
    new_dt = initial_dt
    tc = 0
    for identifier in to_be_vaccinated:
        scheduled_dict.key = identifier
        scheduled_dict.value = new_dt
        scheduled_dict.add(scheduled_dict.key, scheduled_dict.value)
        tc += 1
        if tc > 3:
            time_change = timedelta(minutes=5)
            new_dt = initial_dt + time_change
            tc = 0
            test_dt = new_dt.strftime("%H:%M:%S")
            if int(test_dt[:2]) is 16:
                time_change = timedelta(hours=18, minutes=5)
                new_dt = initial_dt + time_change
    return scheduled_dict
