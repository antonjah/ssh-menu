try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

config = {
    "keywords": "ssh menu interactive",
    "author": "Anton Andersson",
    "description": "A very simple interactive ssh profile menu",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://antonjah.github.io/ssh-menu/",
    "download_url": "https://antonjah.github.io/ssh-menu/",
    "author_email": "contact@antonandersson.se",
    "version": "1.5.2",
    "install_requires": ["bullet"],
    "packages": ["sshmenu"],
    "entry_points": {
        "console_scripts": ['sshmenu = sshmenu.sshmenu:main']
    },
    "name": "ssh-menu",
    "classifiers": [
        "Programming Language :: Python :: 3.6",
    ],
}

setup(**config)
