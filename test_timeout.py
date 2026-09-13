import time

from resilience.timeout_utils import (
    run_with_timeout
)

def slow_function():

    print("Starting...")

    time.sleep(10)

    return "Finished"

try:

    result = run_with_timeout(
        slow_function,
        timeout=3
    )

    print(result)

except TimeoutError as e:

    print("\nTIMEOUT DETECTED")
    print(e)