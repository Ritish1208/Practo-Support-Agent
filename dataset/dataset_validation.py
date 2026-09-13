import json
from collections import Counter
with open("dataset/appointments.json", "r") as file:
    appointments = json.load(file)
print("\nDATASET VALIDATION REPORT")
print("=" * 40)
print(f"Total Records: {len(appointments)}")
category_counts = Counter(
    appointment["category"]
    for appointment in appointments
)
print("\nCategory Distribution:")
for category, count in category_counts.items():
    print(f"{category}: {count}")
status_counts = Counter(
    appointment["status"]
    for appointment in appointments
)
print("\nStatus Distribution:")
for status, count in status_counts.items():
    print(f"{status}: {count}")
follow_up_count = sum(
    appointment["follow_up_required"]
    for appointment in appointments
)
follow_up_percentage = (
    follow_up_count / len(appointments)
) * 100
print(
    f"\nFollow-up Percentage: "
    f"{follow_up_percentage:.2f}%"
)
if 10 <= follow_up_percentage <= 30:
    print("PASS: Follow-up percentage is within range.")
else:
    print("FAIL: Follow-up percentage is outside range.")