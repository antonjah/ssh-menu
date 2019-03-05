#!/usr/bin/env python

import re
import sys
from os import name, system, execvp
from os.path import expanduser

from bullet import Bullet, colors


def main():
    config_dir = expanduser("~/.ssh/config")
    hosts = _get_ssh_hosts(config_dir)

    cli = Bullet(
        choices=hosts,
        indent=0,
        align=4,
        margin=2,
        bullet="🖥",
        bullet_color=colors.bright(colors.foreground["cyan"]),
        word_color=colors.bright(colors.foreground["red"]),
        word_on_switch=colors.bright(colors.foreground["red"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right=5,
    )

    _clear()
    print("\n    Choose ssh profile:")
    result = cli.launch()

    _clear()
    if result == "exit":
        sys.exit()

    if len(result.split(" ")) > 1:
        result = result.split(" ")[0]

    try:
        execvp("ssh", args=["ssh", result])
    except Exception as e:
        sys.exit(e)


def _get_ssh_hosts(config_dir):
    """ Parse lines from ssh config """
    try:
        with open(config_dir, "r") as fh_:
            lines = fh_.read().splitlines()
    except IOError:
        sys.exit("No configuration file found.")

    hosts_ = ["exit"]
    for line in lines:
        kv_ = _key_value(line)
        if len(kv_) > 1:
            key, value = kv_
            if key.lower() == "host":
                hosts_.append(value)
    return hosts_


def _key_value(line):
    """ Parse lines and make sure it's not commented """
    no_comment = line.split("#")[0]
    return [x.strip() for x in re.split(r"\s+", no_comment.strip(), 1)]


def _clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")
