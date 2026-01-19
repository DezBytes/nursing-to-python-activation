# Nurse Logic Gate: Activation Date 12/29/2025
def check_patient_status(hr):
    if hr > 100:
        return "Tachycardia Detected - Pattern Recognition Active"
    elif hr < 60:
        return "Bradycardia Detected - Check Lead Placement"
    else:
        return ("Sinus Rhythm - System Normal")

# Test the logic
patient_hr = 105
print(f"Current Vitals: {check_patient_status(patient_hr)}")