
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ssh-menu',
    'author': 'Anton Andersson',
    'url': 'https://github.com/antonjah/ssh-menu',
    'download_url': 'https://github.com/antonjah/ssh-menu',
    'author_email': 'contact@antonandersson.se',
    'version': '1.0',
    'install_requires': ['console-menu', 'sshconf'],
    'packages': ['ssh-menu'],
    'scripts': ['bin/ssh-menu'],
    'name': 'ssh-menu'
}

setup(**config)
