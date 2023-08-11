import time


def poll(func, timeout=20, interval=1, *args, **kwargs):
    """
    Repeatedly call a function (with arguments) until it returns True or the timeout is exceeded.

    :param func: The function to be polled.
    :param timeout: The maximum time to poll for, in seconds.
    :param interval: The interval between polling, in seconds.
    :param args: Positional arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    :return: True if the function returned True within the timeout, otherwise False.
    """
    end_time = time.time() + timeout
    while time.time() < end_time:
        if func(*args, **kwargs):
            return True
        time.sleep(interval)
    return False
