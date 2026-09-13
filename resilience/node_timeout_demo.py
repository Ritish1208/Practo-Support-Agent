import time
import concurrent.futures


def slow_node():

    print("NODE STARTED")

    time.sleep(10)

    print("NODE FINISHED")

    return "Success"


NODE_TIMEOUT = 3


if __name__ == "__main__":

    print("NODE TIMEOUT DEMO")

    with concurrent.futures.ThreadPoolExecutor() as executor:

        future = executor.submit(
            slow_node
        )

        try:

            result = future.result(
                timeout=NODE_TIMEOUT
            )

            print(result)

        except concurrent.futures.TimeoutError:

            print(
                f"Node timeout exceeded ({NODE_TIMEOUT} seconds)"
            )