import copy


def AUC_ROC_mod(*, label, pred):
    values = sorted(list(zip(label, pred)), key=lambda el: -el[1])
    estimates = [l[0] for l in list(values)]
    ones = 0
    zeros = 0
    numerator = 0
    for estimate in estimates:
        if estimate == 1:
            ones += 1
            continue
        zeros += 1
        numerator += ones
    if ones == 0 or zeros == 0:
        return None
    return numerator / (ones * zeros)

