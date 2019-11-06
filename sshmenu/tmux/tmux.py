from os import execvp
from subprocess import check_call, check_output

from ..decorators import decorators


@decorators.tmux
def ssh_window(host):
    tmux_windows = (
        check_output(["tmux", "list-windows", "-F", "#{window_index},#{window_name}"])
        .decode("utf-8")
        .split()
    )

    window_ids = [
        window_id
        for (window_id, host_) in [window.split(",") for window in tmux_windows]
        if host_ == "ssh:" + host
    ]

    if len(window_ids) > 0:
        execvp("tmux", args=["tmux", "select-window", "-t", window_ids[0]])
    else:
        execvp("tmux", args=["tmux", "new-window", "-n", "ssh:" + host, "ssh " + host])
