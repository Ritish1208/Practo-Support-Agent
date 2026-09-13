import time
import random

MAX_ATTEMPTS = 5
INITIAL_INTERVAL = 1
MAX_INTERVAL = 8
JITTER = True


def run_with_retry(
    func,
    *args,
    max_attempts=MAX_ATTEMPTS,
    initial_interval=INITIAL_INTERVAL,
    max_interval=MAX_INTERVAL,
    jitter=JITTER,
    **kwargs
):
    """
    Executes a function with
    exponential backoff retry.
    """

    delay = initial_interval

    for attempt in range(1, max_attempts + 1):

        try:

            return func(*args, **kwargs)

        except Exception as e:

            print(
                f"[Retry {attempt}/{max_attempts}] Error: {e}"
            )

            if attempt == max_attempts:
                raise

            sleep_time = delay

            if jitter:
                sleep_time += random.uniform(
                    0,
                    0.5
                )

            print(
                f"Retrying in {round(sleep_time,2)} seconds..."
            )

            time.sleep(sleep_time)

            delay = min(
                delay * 2,
                max_interval
            )