from models.infectious import Infectious
class Covid (Infectious):
    def __init__(self):
        super().__init__(name="COVID-19",
                         common_symptoms=["fever", "dry cough", "fatigue", "loss of taste", "loss of smell", "shortness of breath"],
                         severity="Severe",
                         treatment="Management focuses on supportive care, oxygen therapy when needed, antivirals in selected cases, and vaccination for prevention of severe disease.",
                         transmission_method="Airborne droplets",
                         incubation_period="2-14 days")