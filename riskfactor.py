while True:
    M = float(input('Mortalität als Dezimalzahl'))
    I = float(input('Infektionswahrscheinlichkeit beim x Minuten in einem x großen Raum mit einer infizierten Person aufhalten'))
    A = float(input('gefährdetste Altersstufe'))
    In = float(input('Inkubationszeit in Tagen(Durchschnitt)'))
    IA = float(input('Anstecken in Inkubationszeit? nicht anstecken = 0.1 Ansteckend = 1'))
    if A > 60:
        A1 = 0.3
    if A > 30 and A <= 60:
        A1 = 0.5
    if A <= 30:
        A1 = 1

    alpha = 0.4
    beta = 0.4
    delta = 0.1
    gamma = 0.1

    riskscale = M*alpha + I*beta + A1*delta + In*gamma*IA

    print(riskscale)

    """
    Kriterien zur Bewertung des Gesundheitssystems basierend auf den Kriterien der 
    Joint Commission on Accreditation of Healthcare Organizations (JCAHO):
    
    - Zugänglichkeit der Versorgung
    - Angemessenheit der Versorgung
    - Stetigkeit/Koordination der Versorgung
    - Wirksamkeit unter Idealbedingungen (Efficacy of care)
    - Wirksamkeit in der Versorgungspraxis (Effectiveness of care)
    - Wirtschaftlichkeit der Versorgung (Efficiency of care)
    - Patientenorientierung der Versorgung
    - Sicherheit der Versorgungsumgebung
    - Rechtzeitigkeit der Versorgung
    
    Meine Vorschläge für konkrete Zahlen: 
    
    - Ärzte pro Einwohner
    - Krankenhausbetten pro Einwohner
    - BIP
    - Bevölkerungsdichte
    """
    addSystem = bool(input("Systemscore berechnen?"))
    if addSystem:
        doctors_per_person = float(input("Ärzte pro Einwohner:"))
        beds_per_person = float(input("Krankenhausbetten pro Einwohner:"))
        bip = float(input("BIP:"))
        population_density = float(input("Bevölkerungsdichte:"))

        systemscore = (doctors_per_person * beds_per_person * bip)/population_density
        print(population_density)
