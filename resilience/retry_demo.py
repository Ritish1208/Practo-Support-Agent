import time
import random

attempt_counter = 0

MAX_ATTEMPTS = 5
INITIAL_INTERVAL = 1
MAX_INTERVAL = 8
JITTER = True


def flaky_node():
    global attempt_counter

    attempt_counter += 1

    print(f"\nAttempt {attempt_counter}")

    if attempt_counter < 3:
        raise Exception("Simulated transient failure")

    return "Success"


def run_with_retry():

    delay = INITIAL_INTERVAL

    for attempt in range(MAX_ATTEMPTS):

        try:
            result = flaky_node()

            print("\nRecovered Successfully")
            print("Result:", result)

            return

        except Exception as e:

            print("Error:", e)

            if attempt == MAX_ATTEMPTS - 1:
                print("\nMaximum retry attempts reached")
                return

            sleep_time = delay

            if JITTER:
                sleep_time += random.uniform(0, 0.5)

            print(
                f"Retrying in {round(sleep_time,2)} seconds..."
            )

            time.sleep(sleep_time)

            delay = min(
                delay * 2,
                MAX_INTERVAL
            )


if __name__ == "__main__":

    print("RETRY POLICY DEMO")

    print(
        f"Max Attempts = {MAX_ATTEMPTS}"
    )

    print(
        f"Initial Interval = {INITIAL_INTERVAL}s"
    )

    print(
        f"Max Interval = {MAX_INTERVAL}s"
    )

    print(
        f"Jitter Enabled = {JITTER}"
    )

    run_with_retry()