import concurrent.futures


def run_with_timeout(
    func,
    *args,
    timeout=5,
    **kwargs
):
    """
    Executes a function with timeout protection.
    """

    with concurrent.futures.ThreadPoolExecutor() as executor:

        future = executor.submit(
            func,
            *args,
            **kwargs
        )

        try:

            return future.result(
                timeout=timeout
            )

        except concurrent.futures.TimeoutError:

            raise TimeoutError(
                f"Function exceeded {timeout} seconds"
            )


def run_agent_with_global_timeout(
    agent,
    input_data,
    config,
    timeout=15
):

    return run_with_timeout(
        agent.invoke,
        input_data,
        config=config,
        timeout=timeout
    )