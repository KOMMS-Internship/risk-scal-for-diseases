def calculate_infection_probability(meter, minutes, probability):
    return meter/2*minutes/2*probability/2  # Todo

def risk_scale_disease(mortality: float, infection_probability: float, risk_group: int, inkubation: int,
               infectious_inkubation: bool, alpha: float = 0.4, beta:float = 0.4, delta:float = 0.1,
                       gamma:float = 0.1) -> float:
    """
    :param mortality: as percentage
    :param infection_probability: per x minutes in a x m big area with a infected person
    :param risk_group: the age group with the highest mortality
    :param inkubation: inkubation time in average
    :param infectious_inkubation: Is a infected person infectious during the inkubation time
    :param alpha: #Todo Rasmus
    :param beta: #Todo Rasmus
    :param gamma: #Todo Rasmus
    :param delta: #Todo Rasmus
    :return: the calculated dangerousness in our risk scale
    """

    if infectious_inkubation:
        infectious_inkubation =  1
    else:
        infectious_inkubation = 0.1

    if risk_group > 60:
        risk_group = 0.3
    elif 30 < risk_group <= 60:
        risk_group = 0.5
    elif risk_group <= 30:
        risk_group = 1

    return mortality*alpha + infection_probability*beta + risk_group*delta + inkubation*gamma*infectious_inkubation


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

def health_system_score(doctors_per_person: float, hospital_beds_per_person: float, bip_for_health: float,
                        population_density: float, alpha_groß: float = 1, beta_groß: float = 1, gamma_groß: float = 1,
                        epsilon: float = 1) -> float:

    """
    :param doctors_per_person:
    :param hospital_beds_per_person:
    :param bip_for_health: How much money of the bip is spended for health
    :param population_density:
    :return: healty system score
    """

    return (doctors_per_person * beds_per_person * bip_for_health)/population_density
