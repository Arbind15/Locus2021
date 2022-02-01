import math
from datetime import datetime, date, timedelta

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
    global  to_be_vaccinated
    total_registered = len(priority_1) + len(priority_0)
    no_of_hri = int((percent_of_hri / 100) * available_no_vaccine)
    no_of_general = available_no_vaccine - no_of_hri
    print(priority_1[:no_of_hri])
    to_be_vaccinated = priority_1[:no_of_hri] + priority_0[:no_of_general]


def scheduler(vaccination_date, dob, health_status, identifier, percent_of_hri, available_no_vaccine):
    priority_assigner({'dob': dob, 'health_stats': health_status, 'id': identifier})
    print(priority_0, priority_1)
    queue_generator(percent_of_hri, available_no_vaccine)
    print(to_be_vaccinated)
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
    return scheduled_dict


print(scheduler("2045-04-03", "2005-04-03",1,5,10,1230))