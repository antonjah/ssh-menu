from os import environ

IS_TMUX_SESSION = "TMUX" in environ

def tmux(func):
    def wrapper(*args, **kwargs):
        if IS_TMUX_SESSION:
            func(*args, **kwargs)

    return wrapper