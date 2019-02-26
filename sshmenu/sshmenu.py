#!/usr/bin/env python

import re
import subprocess
import sys
from os import name, system
from os.path import expanduser

from bullet import Bullet, colors


def main():
    home = expanduser("~/.ssh/config")
    hosts = _get_ssh_hosts(home)

    cli = Bullet(
        choices=hosts, 
        indent=0,
        align=5, 
        margin=2,
        bullet="🖥",
        bullet_color=colors.bright(colors.foreground["cyan"]),
        word_color=colors.bright(colors.foreground["red"]),
        word_on_switch=colors.bright(colors.foreground["red"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right = 5
    )

    clear()
    result = cli.launch()

    if result == "exit":
        clear()
        sys.exit()

    try:
        clear()
        subprocess.call("ssh {}".format(result), shell=True)
    except Exception as e:
        sys.exit(e)


def _get_ssh_hosts(home):
    """ Parse lines from ssh config """
    try:
        with open(home, "r") as fh_:
            lines = fh_.read().splitlines()
    except IOError:
        sys.exit("Can't find ssh config")

    hosts_ = ["exit"]
    for line in lines:
        kv_ = _key_value(line)
        if len(kv_) > 1:
            key, value = kv_
            if key.lower() == "host":
                hosts_.append(value)
    return hosts_


def _key_value(line):
    """ Parse line key value and make sure it's not a comment """
    no_comment = line.split("#")[0]
    return [x.strip() for x in re.split(r"\s+", no_comment.strip(), 1)]


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")
