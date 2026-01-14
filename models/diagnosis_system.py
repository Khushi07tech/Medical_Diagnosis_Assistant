from models.Diseases.flu import Flu
from models.Diseases.diabetes import Diabetes
from models.Diseases.migraine import Migraine

class DiagnosisSystem:
    def __init__(self):
        self.diseases = []

    def add_disease(self, disease):
        self.diseases.append (disease)

    def load_diseases(self):
        flu = Flu ()
        diabetes = Diabetes ()
        migraine = Migraine ()

        self.add_disease(flu)
        self.add_disease(diabetes)
        self.add_disease(migraine)

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

        for result in results[:3]:

           disease = result ['disease']
           percentage = result['match_percentage']

           print (f"{disease.name}: {percentage:.2f}%")
           print (f"Recommendation: {disease.get_recommendation()}")
           print ("*" * 35)
        print("Not a substitute for a medical advice!")
