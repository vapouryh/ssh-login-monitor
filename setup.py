#                     GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007
#                       
# SSH Login Monitor - Monitors your login info on linux sever.
# Copyright (C) 2021 - vapouryh
#
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

import setuptools

with open("README.md", "r") as readme:

    long_description = readme.read()

setuptools.setup(
    name='SSH Login Live',
    version='1.0',
    author='vapouryh',
    description="SSH Login Monitor for Ubuntu Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vapouryh/ssh-login-live',
    packages=setuptools.find_packages(),
    install_requires =[ 
        'paramiko', 
        'pyyaml',
        'paramiko_expect', 
    ],
    python_requires='>=3.9',
)
