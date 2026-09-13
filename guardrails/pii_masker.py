import re

def mask_phone_numbers(text):

    pattern = r"\b\d{10}\b"

    def replace(match):
        number = match.group()
        return number[:2] + "******" + number[-2:]

    return re.sub(
        pattern,
        replace,
        text
    )
sample = ("My phone number is 9876543210"
          )
print(
    mask_phone_numbers(sample)
)