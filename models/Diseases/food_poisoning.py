from models.acute import Acute
class Food_Poisoning (Acute):
    def __init__(self):
        super().__init__(name="Food Poisoning",
                         common_symptoms=["nausea", "vomiting", "diarrhea", "stomach cramps", "fever"],
                         severity="Mild",
                         treatment="Primarily managed with rehydration, rest, and supportive care, with antibiotics reserved for severe or specific bacterial infections.",
                         onset_speed="Sudden (within hours)",
                         typical_duration="1-3 days")