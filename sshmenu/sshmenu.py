#!/usr/bin/env python3

import re
import sys
from collections import OrderedDict
from os import execvp, name, system
from os.path import expanduser

from bullet import Bullet, colors
from .tmux import tmux


def main():
    ssh_config = expanduser("~/.ssh/config")
    hosts = _get_ssh_hosts(ssh_config)

    host = _render_menu(hosts)

    _clear()

    if host == "exit":
        sys.exit(0)
    elif len(host.split(" ")) > 1:
        host = host.split(" ")[0]

    print("Connecting to {} ...".format(host))

    try:
        tmux.ssh_window(host)
        execvp("ssh", args=["ssh", host])
    except Exception as e:
        sys.exit(e)


def _render_menu(hosts):
    cli = Bullet(
        choices=list(hosts + ["exit"]),
        indent=0,
        align=4,
        margin=2,
        bullet=">",
        bullet_color=colors.bright(colors.foreground["cyan"]),
        background_on_switch=colors.background["black"],
        word_color=colors.bright(colors.foreground["red"]),
        word_on_switch=colors.bright(colors.foreground["red"]),
        pad_right=5,
    )

    _clear()

    print("\n    Choose ssh profile:")

    return cli.launch()


def _get_ssh_hosts(config_dir):
    """ Parse lines from ssh config """
    try:
        with open(config_dir, "r") as fh_:
            lines = fh_.read().splitlines()
    except IOError:
        sys.exit("No configuration file found.")

    hosts_ = []
    for line in lines:
        kv_ = _key_value(line)
        if len(kv_) > 1:
            key, value = kv_
            if key.lower() == "host" and value != "*":
                hosts_.append(value)
    return hosts_


def _key_value(line):
    """ Parse lines and make sure it's not commented """
    no_comment = line.split("#")[0]
    return [x.strip() for x in re.split(r"\s+", no_comment.strip(), 1)]


def _clear():
    """ Clear buffer """
    if name == "nt":
        system("cls")
    else:
        system("clear")
