from models.infectious import Infectious
class Cold (Infectious):
    def __init__(self):
        super().__init__(name="Common Cold",
                         common_symptoms=["runny nose", "sneezing", "sore throat", "mild cough", "mild fatigue"],
                         severity="Mild",
                         treatment="Managed with rest, fluids, and symptomatic relief using antipyretics and decongestants, as it is usually self-limiting.",
                         transmission_method="Airborne Droplets",
                         incubation_period="1-3 days")