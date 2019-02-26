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
    "url": "https://github.com/antonjah/ssh-menu",
    "download_url": "https://github.com/antonjah/ssh-menu",
    "author_email": "contact@antonandersson.se",
    "version": "1.4.1",
    "install_requires": ["bullet"],
    "packages": ["sshmenu"],
    "entry_points": {
        "console_scripts": ['sshmenu = sshmenu.sshmenu:main']
    },
    "name": "ssh-menu",
    "classifiers": [
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 2.7",
    ],
}

setup(**config)
