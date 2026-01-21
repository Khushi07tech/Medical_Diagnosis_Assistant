from models.Diseases.flu import Flu
from models.Diseases.diabetes import Diabetes
from models.Diseases.migraine import Migraine
from models.Diseases.covid import Covid
from models.Diseases.appendicitis import Appendicitis
from models.Diseases.asthma import Asthma
from models.Diseases.cold import Cold
from models.Diseases.food_poisoning import Food_Poisoning
from models.Diseases.hypertension import Hypertension

class DiagnosisSystem:
    def __init__(self):
        self.diseases = []

    def add_disease(self, disease):
        self.diseases.append (disease)

    def load_diseases(self):
        flu = Flu ()
        diabetes = Diabetes ()
        migraine = Migraine ()
        covid = Covid ()
        appendicitis = Appendicitis ()
        asthma = Asthma ()
        cold = Cold ()
        food_poisoning = Food_Poisoning ()
        hypertension = Hypertension()

        self.add_disease(flu)
        self.add_disease(diabetes)
        self.add_disease(migraine)
        self.add_disease(covid)
        self.add_disease(appendicitis)
        self.add_disease(asthma)
        self.add_disease(cold)
        self.add_disease(food_poisoning)
        self.add_disease(hypertension)

    def diagnose (self, user_symptoms):
        results = []
        for disease in self.diseases:
            percentage = disease.check_symptoms(user_symptoms)
            info_and_percentage = {'disease': disease,
                                   'match_percentage': percentage}
            results.append (info_and_percentage)
        return sorted(results, key= lambda x: x['match_percentage'], reverse=True)

    def display_diagnosis (self, results):
        if not results:
            print("No matches found")
            return

        print ("=====DIAGNOSIS=====")

        for result in results[:2]:

           disease = result ['disease']
           percentage = result['match_percentage']

           print (f"{disease.name}: {percentage:.2f}%")
           print (f"Recommendation: {disease.get_recommendation()}")
           print ("*" * 35)
        print("Not a substitute for a medical advice!")
