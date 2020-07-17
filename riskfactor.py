# Wie berech net man die Infektionswahrscheinlichkeit?
def calculate_infection_probability(meter, minutes, probability):
    return  ((minutes / 2) * (probability / 2)) / (meter / 2)


def risk_scale_disease(mortality: float, infection_probability: float, risk_group: int, inkubation: int,
                       infectious_inkubation: bool, alpha: float = 0.4, beta: float = 0.4, delta: float = 0.1,
                       gamma: float = 0.1) -> float:
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
        infectious_inkubation = 1
    else:
        infectious_inkubation = 0.1

    if risk_group > 60:
        risk_group = 0.3
    elif 30 < risk_group <= 60:
        risk_group = 0.5
    elif risk_group <= 30:
        risk_group = 1

    return mortality * alpha + infection_probability * beta + risk_group * delta + inkubation * gamma * \
           infectious_inkubation


def health_system_score(doctors_per_person: float, hospital_beds_per_person: float, bip_for_health: float,
                        population_density: float, infant_mortality: float = 1) -> float:
    """
    :param doctors_per_person:
    :param hospital_beds_per_person:
    :param infant_mortality
    :param bip_for_health: How much money of the bip is spended for health
    :param population_density:
    :return: healty system score
    """
    
    two_digit_multiplier = 1/10
    three_digit_multiplier = 1/100
    four digit_multiplier = 1/1000
    five_digit_multiplier = 1/10000
    six_digit_multiplier = 1/100000

    return (doctors_per_person * hospital_beds_per_person * beds_per_person * bip_for_health) / (population_density * infant_mortality)
