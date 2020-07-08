while True:
    M = float(input('Mortalität als Dezimalzahl'))
    I = float(input('Infektionswahrscheinlichkeit beim x Minuten in einem x großen Raum mit einer infizierten Person aufhalten'))
    A = float(input('gefährdeteste Altersstufe'))
    In = float(input('Inkubationszeit in Tagen(Durchschnitt)'))
    if A > 60:
        A1 = 1
    if A > 30 and A <= 60:
        A1 = 2
    if A <= 30:
        A1 = 3

    alpha = 0.4
    beta = 0.4
    delta = 0.1
    gamma = 0.1

    riskscale = M*alpha + I*beta + A1*delta + In*gamma

    print(riskscale)