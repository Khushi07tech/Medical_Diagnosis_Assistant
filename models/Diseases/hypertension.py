from models.chronic import Chronic
class Hypertension (Chronic):
    def __init__(self):
        super().__init__(name="Hypertension",
                         common_symptoms=["headaches", "dizziness", "blurred vision", "chest pain", "shortness of breath"],
                         severity="Moderate",
                         treatment="Use antihypertensive medications to maintain blood pressure within normal limits and prevent complications.",
                         management_plan= "Regular blood pressure monitoring, medication, low-salt diet, exercise",
                         requires_monitoring= True)