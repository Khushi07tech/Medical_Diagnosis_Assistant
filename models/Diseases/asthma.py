from models.chronic import Chronic
class Asthma (Chronic):
    def __init__(self):
        super().__init__(name="Asthma",
                         common_symptoms=["wheezing", "shortness of breath", "chest tightness", "coughing"],
                         severity="Moderate",
                         treatment="Controlled with inhaled bronchodilators for acute relief and inhaled corticosteroids for long-term inflammation management.",
                         management_plan= "Inhaler use, avoid triggers, regular check-ups",
                         requires_monitoring= True)