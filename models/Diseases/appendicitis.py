from models.acute import Acute
class Appendicitis (Acute):
    def __init__(self):
        super().__init__(name="Appendicitis",
                         common_symptoms=[ "sharp abdominal pain", "nausea", "vomiting", "fever", "loss of appetite"],
                         severity="Severe",
                         treatment="Appendectomy often preceded by antibiotics.",
                         onset_speed="Gradual (hours to days)",
                         typical_duration="1-3 weeks")