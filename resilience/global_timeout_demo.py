import time
import concurrent.futures


def node1():
    print("NODE 1 STARTED")
    time.sleep(3)
    print("NODE 1 FINISHED")


def node2():
    print("NODE 2 STARTED")
    time.sleep(3)
    print("NODE 2 FINISHED")


def node3():
    print("NODE 3 STARTED")
    time.sleep(3)
    print("NODE 3 FINISHED")


GLOBAL_TIMEOUT = 5


def run_workflow():

    node1()
    node2()
    node3()


if __name__ == "__main__":

    print("GLOBAL TIMEOUT DEMO")

    with concurrent.futures.ThreadPoolExecutor() as executor:

        future = executor.submit(
            run_workflow
        )

        try:

            future.result(
                timeout=GLOBAL_TIMEOUT
            )

            print(
                "\nWorkflow completed successfully"
            )

        except concurrent.futures.TimeoutError:

            print(
                f"\nGlobal timeout exceeded ({GLOBAL_TIMEOUT} seconds)"
            )