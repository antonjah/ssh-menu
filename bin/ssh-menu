#!/usr/bin/env python

import sys
from os.path import expanduser

from consolemenu import ConsoleMenu
from consolemenu.items import CommandItem
from sshconf import read_ssh_config


def main():
    # Get all SSH entries
    conf = _init_ssh_conf()
    # Get the hosts
    hosts = conf.hosts()

    # Create the base menu
    menu = ConsoleMenu("ssh-menu", "Current SSH profiles:")

    # Populate the menu from the SSH config
    for host in hosts:
        if len(host.split(" ")) > 1:
            menu.append_item(
                CommandItem(
                    host,
                    "ssh {}".format(host.split(" ")[0]),
                    should_exit=True
                )
            )
        else:
            menu.append_item(
                CommandItem(
                    host,
                    "ssh {}".format(host),
                    should_exit=True
                )
            )

    # Show the menu
    menu.show()


def _init_ssh_conf():
    return read_ssh_config(expanduser("~/.ssh/config"))


if __name__ == "__main__":
    sys.exit(main())
