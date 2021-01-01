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