# <img src="https://cdn.iconscout.com/icon/free/png-256/list-bullets-menu-format-formatting-items-6-3298.png" height="30" width="30"> sshmenu

<img src="img/sshmenu.png">

sshmenu is a *very* simple terminal tool that reads your ssh-config  
and renders an interactive menu with your ssh profiles listed

If sshmenu is executed within a Tmux session, it will automatically create a new pane and connect

## Installation

Requires:

* python3
* pip

Install:

```bash
sudo pip install ssh-menu
```

Uninstall:

```bash
sudo pip uninstall ssh-menu
```

**Note:** sshmenu depends on a config file located in your `/home/user/.ssh` folder  
You can find examples [here](https://linuxize.com/post/using-the-ssh-config-file/)

## Alias

You can alias sshmenu to make it easier to use

Bash:

```bash
echo 'alias ssm="sshmenu"' >> ~/.bashrc
source ~/.bashrc
```

Zsh:

```bash
echo 'alias ssm="sshmenu"' >> ~/.zshrc
source ~/.zshrc
```

Now you can just run `ssm` to open sshmenu

## Docker

Running in docker (why? I don't know):

```bash
docker run -it -v $PWD/config:/root/.ssh/config antonjah/ssh-menu
```

## Contributors

[vkushnir](https://github.com/vkushnir)
