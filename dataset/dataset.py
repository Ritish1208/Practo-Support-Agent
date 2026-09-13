import json
import random
from collections import Counter
SEED = 42
random.seed(SEED)
CATEGORIES = [
"General Medicine",
"Cardiology",
"Dermatology",
"Pediatrics",
"Orthopedics"
]

STATUSES= [
"Scheduled",
"Completed",
"Cancelled",
"No-Show",
"Rescheduled"


]

NUM_RECORDS = 50

def generate_appointment(record_number):
    appointment={
         "record_id": f"APT{1000 + record_number}",
        "category": random.choice(CATEGORIES),
        "status": random.choice(STATUSES),
        "consultation_fee_inr": random.randint(300, 2500),
        "days_since_created": random.randint(0, 30),
        "follow_up_required": random.random() < 0.20
    }
    return appointment

appointments = []
for i in range(1, NUM_RECORDS + 1):
        appointments.append(generate_appointment(i))

with open("appointments.json", "w") as file:
        json.dump(appointments, file, indent=4)

print(f"{NUM_RECORDS} appointments generated successfully!")