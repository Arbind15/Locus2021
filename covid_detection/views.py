import json
from .covid_serializers import CovidSerializers
from django.http import HttpResponse, JsonResponse
from .detection_algorithm import readData, encodeData, removeUnwantedData, calculateInfectionProbability



def detectCovidInfectionProb(req):
    reqBody = json.loads(req.body)
    data = reqBody['data']
    covid = readData()
    covid = encodeData(covid)
    covid = removeUnwantedData(covid)
    # [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1]
    probability = calculateInfectionProbability(covid=covid, data=data)
    return JsonResponse({
        "message": "Infection Probability calculated Successfully",
        "payload": {
            "percentage": probability,
        }
    }, safe=False)

