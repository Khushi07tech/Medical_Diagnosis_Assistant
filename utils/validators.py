def validate_symptoms_input(user_input):
    user_input = user_input.strip()
    if user_input == "":
        return False, "Your input can not be empty/whitespace!"

    if len(user_input) < 3:
        return False, "Enter at least 3 characters!"

    return True, "Valid Input!"

def validate_yes_no_input(user_input):
    user_input = user_input.strip().lower()
    if user_input in ["y", "yes", "yep", "n", "no", "nope"]:
        return True, user_input
    else:
        return False, "Please enter 'y' or 'n'!"

def get_common_symptoms():
    common_symptoms = ["fever", "cough", "headache", "fatigue",
                       "nausea", "vomiting", "diarrhea", "dizziness",
                       "chest pain", "shortness of breath",
                       "sore throat", "runny nose", "body aches",
                       "chills", "sweating", "loss of appetite", "abdominal pain"]
    return common_symptoms

def display_symptom_suggestions():
    print ("============== C O M M O N   S Y M P T O M S ==============")
    symptoms = get_common_symptoms()
    for i in range(0, len(symptoms), 5):
        print (", ".join(symptoms[i:i+5]))
    print ("============================================================")





