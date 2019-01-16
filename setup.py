
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

config = {
    'description': 'ssh-menu',
    'keywords': 'ssh menu interactive',
    'author': 'Anton Andersson',
    'description': 'A very simple interactive ssh profile menu',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'url': 'https://github.com/antonjah/ssh-menu',
    'download_url': 'https://github.com/antonjah/ssh-menu',
    'author_email': 'contact@antonandersson.se',
    'version': '1.2.2',
    'install_requires': ['console-menu', 'sshconf'],
    'packages': ['ssh-menu'],
    'scripts': ['bin/ssh-menu'],
    'name': 'ssh-menu'
}

setup(**config)
