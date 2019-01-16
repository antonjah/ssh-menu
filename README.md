# <img src="https://cdn.iconscout.com/icon/free/png-256/list-bullets-menu-format-formatting-items-6-3298.png" height="30" width="30"> ssh-menu

ssh-menu is a *very* simple terminal client that reads your ssh-config  
and renders an interactive menu with your ssh profiles listed

## Installation

Install:

```bash
pip install ssh-menu
```

Uninstall:

```bash
pip uninstall ssh-menu
```

**Note:** ssh-menu depends on a config file located in your *home/.ssh-folder  
You can find examples [here](https://www.ssh.com/ssh/config/)

## Docker

Running in docker (why? I don't know):

```bash
docker run -it -v $PWD/config:/root/.ssh/config antonjah/ssh-menu
```

## Todo

* Enable adding profiles
* Custom profile location
* Handle output even if session dies unexpectedly


### Dependencies

* [sshconf](https://pypi.org/project/sshconf/)
* [console-menu](https://pypi.org/project/console-menu/)
