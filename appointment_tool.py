import json
import os

JSON_PATH = os.path.join(
    "dataset",
    "appointments.json"
)

with open(JSON_PATH, "r", encoding="utf-8") as file:
    appointments = json.load(file)


def check_appointment_status(record_id):

    for appointment in appointments:

        if appointment["record_id"] == record_id:

            recency_score = (
                appointment["days_since_created"] / 30
            )

            followup_score = (
                1 if appointment["follow_up_required"]
                else 0
            )

            escalation_score = round(
                (0.6 * followup_score)
                +
                (0.4 * recency_score),
                2
            )

            return {
                "record_id": record_id,
                "status": appointment["status"],
                "consultation_fee_inr":
                    appointment["consultation_fee_inr"],
                "escalation_score":
                    escalation_score
            }

    return {
        "error": "Record not found"
    }


print(
    check_appointment_status(
        appointments[0]["record_id"]
    )
)

print(
    check_appointment_status(
        appointments[5]["record_id"]
    )
)

print(
    check_appointment_status(
        "INVALID"
    )
)