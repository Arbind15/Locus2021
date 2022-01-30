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

toltal_pop = {
    'sunasri': 20000,
    'morang': 100000,
    'jhapa': 2560,
    'illam': 350000,
    'dolpa': 1060540,
    'manang': 5000000,
}


def CalculateInfectionRate(initial_infect, final_infect):
    # print(initial_infect.items())
    d = {}
    for lbl1, num1, lbl2, num2 in zip(initial_infect.keys(), initial_infect.values(), final_infect.keys(),
                                      final_infect.values()):
        diff = num2 - num1
        if diff < 0:
            diff = 0
        d[lbl1] = diff
        # print(diff)
    return d


def CalculateInfectionRatio(total_pop, final_infect):
    # print(initial_infect.items())
    d = {}
    for lbl1, num1, lbl2, num2 in zip(total_pop.keys(), total_pop.values(), final_infect.keys(),
                                      final_infect.values()):
        ratio = num2 / num1
        d[lbl1] = ratio
    return d


def DistributeVaccine(infectionRate, finale, totalVaccine=500000):
    d = {}
    assigned_vaccine = {}

    # rateSum = 0
    # ratioSum = 0
    # for num in infectionRate.values():
    #     rateSum = rateSum + num
    # print('rate sum', rateSum)
    #
    # for num in finale.values():
    #     ratioSum = ratioSum + num
    # print('ratio sum', ratioSum)

    rateParm = 500
    ratioParm = 1

    for lbl, num1, num2 in zip(infectionRate.keys(), infectionRate.values(), finale.values()):
        d[lbl] = num1 * rateParm + num2 * ratioParm

    final_sum = 0
    for num in d.values():
        final_sum += num

    for lbl, num in zip(d.keys(), d.values()):
        ratio = num / final_sum
        d[lbl] = ratio
        assigned_vaccine[lbl] = math.floor(ratio * totalVaccine)

    print(d)
    print(assigned_vaccine)

    # ratio = 0
    # for lbl, num in zip(infectionRate.keys(), infectionRate.values()):
    #     ratio = num / rateSum
    #     assigned_vaccine[lbl] = math.floor(ratio * totalVaccine)
    #     d[lbl] = ratio
    # print(d)
    # print(assigned_vaccine)


print(CalculateInfectionRate(initial, finanal))
# print(CalculateInfectionRatio(toltal_pop, finanal))

DistributeVaccine(CalculateInfectionRate(initial, finanal), finanal)
