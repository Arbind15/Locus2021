import json, random,os
from covidResponse.settings import MEDIA_ROOT

# Data to be written
districts = [
    "achham",
    "arghakhanchi",
    "baglung",
    "baitadi",
    "bajhang",
    "bajura",
    "banke",
    "bara",
    "bardiya",
    "bhaktapur",
    "bhojpur",
    "chitwan",
    "dadeldhura",
    "dailekh",
    "dang deukhuri",
    "darchula",
    "dhading",
    "dhankuta",
    "dhanusa",
    "dholkha",
    "dolpa",
    "doti",
    "gorkha",
    "gulmi",
    "humla",
    "ilam",
    "jajarkot",
    "jhapa",
    "jumla",
    "kailali",
    "kalikot",
    "kanchanpur",
    "kapilvastu",
    "kaski",
    "kathmandu",
    "kavrepalanchok",
    "khotang",
    "lalitpur",
    "lamjung",
    "mahottari",
    "makwanpur",
    "manang",
    "morang",
    "mugu",
    "mustang",
    "myagdi",
    "nawalparasi",
    "nuwakot",
    "okhaldhunga",
    "palpa",
    "panchthar",
    "parbat",
    "parsa",
    "pyuthan",
    "ramechhap",
    "rasuwa",
    "rautahat",
    "rolpa",
    "rukum",
    "rupandehi",
    "salyan",
    "sankhuwasabha",
    "saptari",
    "sarlahi",
    "sindhuli",
    "sindhupalchok",
    "siraha",
    "solukhumbu",
    "sunsari",
    "surkhet",
    "syangja",
    "tanahu",
    "taplejung",
    "terhathum",
    "udayapur"
]

initialInfPop = {}
finalInfPop={}

for lbl in districts:
    initialInfPop[lbl]=random.randint(5000,500000)
    finalInfPop[lbl]=random.randint(500,500000)

# Serializing json
json_object = json.dumps(initialInfPop, indent=4)
# Writing to sample.json
data_loc=os.path.join(MEDIA_ROOT,'data')
with open(data_loc+"/initialInfPop.json", "w") as outfile:
    outfile.write(json_object)

# Serializing json
json_object = json.dumps(finalInfPop, indent=4)
# Writing to sample.json
with open(data_loc+"/finalInfPop.json", "w") as outfile:
    outfile.write(json_object)
