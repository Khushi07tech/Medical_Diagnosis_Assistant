from models.diagnosis_system import DiagnosisSystem
def main ():
    system = DiagnosisSystem()

    print ("-----Medical Diagnosis Assistant-----")
    user_name = input ("Enter your name: ").title()
    print(f"Welcome {user_name}")

    is_running = True

    while is_running:
        user_symptoms = input ("Enter your symptoms seprated by comma: ")
        user_symptoms = user_symptoms.split(",")
        clean_symptoms = [symptom.strip().lower() for symptom in user_symptoms]

        results = system.diagnose(clean_symptoms)
        system.display_diagnosis(results)

        run_again = input ("Do you want to ask again? (Yes/No): ").lower()
        if run_again == "no":
            is_running = False
            print ("Ba bye!")
if __name__ == '__main__':
    main ()

