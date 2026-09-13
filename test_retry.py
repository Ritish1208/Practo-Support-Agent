from resilience.retry_utils import run_with_retry

counter = 0

def flaky():

    global counter

    counter += 1

    if counter < 3:
        raise Exception("Temporary Failure")

    return "Success"


print(
    run_with_retry(flaky)
)