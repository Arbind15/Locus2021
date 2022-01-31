import json, os, datetime
from covidResponse.settings import MEDIA_ROOT
from authentication.models import userProfile, hospitalProfile, adminProfile
from django.contrib.auth.models import User

def registerHospitalFromFile():
    data_loc = os.path.join(MEDIA_ROOT, 'data')
    with open(data_loc + '/initialInfPop.json', 'r') as openfile:
        qParms = json.load(openfile)

    default_password='123'
    # print(qParms.keys())
    for lbl in qParms.keys():
        usr = User.objects.create_user(username=lbl, email='', password=default_password)
        pro = hospitalProfile(username=usr, Address=lbl)
        pro.save()
        hospitalProfile.refresh_from_db(pro)

registerHospitalFromFile()