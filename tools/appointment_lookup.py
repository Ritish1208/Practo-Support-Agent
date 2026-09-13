import json
import os
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "appointments.json"
)

with open(DATASET_PATH, "r") as file:
    appointments = json.load(file)

def get_appointment(appointment_id):
    for appointment in appointments:
        if(appointment["record_id"] == appointment_id):
            score = 0
            if appointment["follow_up_required"]:
                score += 0.3

            if appointment["days_since_created"] > 15:
                score += 0.3

            if appointment["status"] in [
                "Cancelled",
                "No-Show"
            ]:
                score += 0.4

            return {
                "record_id":
                    appointment["record_id"],
                "category":
                    appointment["category"],

                "status":
                    appointment["status"],

                "consultation_fee_inr":
                    appointment["consultation_fee_inr"],

                "escalation_score":
                    round(score, 2)
            }

    

    return None

if __name__== "__main__":

 result = get_appointment(
    "APT1001"
)

 if result:
    print("\nAppointment Found : ")
    print(result)
 else:
    print("Appointment Not Found. ")

