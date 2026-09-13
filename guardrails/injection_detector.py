def detect_injection(text):

    suspicious_phrases = [

        "ignore previous instructions",

        "forget your rules",

        "reveal system prompt",

        "bypass guardrails"
    ]

    text = text.lower()

    for phrase in suspicious_phrases:

        if phrase in text:
            return True

    return False

print(detect_injection(
    "Ignore previous instructions"
))