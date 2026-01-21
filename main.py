from models.diagnosis_system import DiagnosisSystem
from utils.validators import validate_symptoms_input, validate_yes_no_input, display_symptom_suggestions

def main ():
    system = DiagnosisSystem()
    system.load_diseases()
    print ("-----Medical Diagnosis Assistant-----")
    user_name = input ("Enter your name: ").title()
    print(f"Welcome {user_name}")

    is_running = True

    while is_running:
        while True:
            user_help = input ("Need help? Type 'help' to see common symptoms, or press Enter to continue: ").lower()
            if user_help == "help":
                display_symptom_suggestions()
                break
            else:
                break

        while True:
            user_symptoms = input ("Enter your symptoms seprated by comma: ")
            is_valid, message = validate_symptoms_input(user_symptoms)
            if is_valid:
                break
            else:
                print (message)

        user_symptoms = user_symptoms.split(",")
        clean_symptoms = [symptom.strip().lower() for symptom in user_symptoms]

        results = system.diagnose(clean_symptoms)
        system.display_diagnosis(results)

        while True:
            run_again = input ("Do you want to ask again? (Yes/No): ").lower()
            is_valid, response = validate_yes_no_input(run_again)
            if is_valid:
                if response in ["n", "no", "nope"]:
                    is_running = False
                break
            else:
                print (response)

if __name__ == '__main__':
    main ()