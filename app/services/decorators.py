def run_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            func(*args, **kwargs)
            wrapper.has_run = True

    wrapper.has_run = False
    return wrapper
