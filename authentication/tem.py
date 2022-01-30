import math

initial = {
    'sunasri': 5000,
    'morang': 100,
    'jhapa': 20,
    'illam': 35000,
    'dolpa': 10540,
    'manang': 500000,
}
finanal = {
    'sunasri': 200,
    'morang': 1000,
    'jhapa': 19,
    'illam': 3500,
    'dolpa': 1000540,
    'manang': 50,
}


def CalculateInfectionRate(initial_infect, final_infect):
    d = {}
    for lbl1, num1, lbl2, num2 in zip(initial_infect.keys(), initial_infect.values(), final_infect.keys(),
                                      final_infect.values()):
        diff = num2 - num1
        if diff < 0:
            diff = 0
        d[lbl1] = diff
    return d


def DistributeVaccine(infectionRate, finale, totalVaccine=500000):
    d = {}
    assigned_vaccine = {}

    # weight for infection rate
    rateParm = 0.2

    # weight for total infection
    ratioParm = 0.8

    final_sum = 0
    for lbl, num1, num2 in zip(infectionRate.keys(), infectionRate.values(), finale.values()):
        nn = num1 * rateParm + num2 * ratioParm
        final_sum += nn
        d[lbl] = nn

    for lbl, num in zip(d.keys(), d.values()):
        ratio = num / final_sum
        d[lbl] = ratio
        assigned_vaccine[lbl] = math.floor(ratio * totalVaccine)

    # print(d)
    print(assigned_vaccine)

    return assigned_vaccine


# print(CalculateInfectionRate(initial, finanal))

DistributeVaccine(CalculateInfectionRate(initial, finanal), finanal)
