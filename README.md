![GitHub](https://img.shields.io/github/license/vapouryh/ssh-login-monitor?style=for-the-badge)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/vapouryh/ssh-login-monitor?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/vapouryh/ssh-login-monitor?style=for-the-badge)

**To install:**

See the releases tab on the [GitHub Page](https://github.com/vapouryh/ssh-login-monitor) or [CLICK HERE](https://github.com/vapouryh/ssh-login-monitor/releases)

**Prerequisites:**

1. You must have at least Python 3.9 with pip/pip3 [INSTALL HERE](https://www.python.org/downloads/)
2. Have an Ubuntu Server with an account that has sudo commands/access (Program hasn't been tested on other Linux Distros)

**To Setup:**

1. Edit config.yaml and enter your server details as followed in the example file (config_example.yaml)
2. Open a terminal.
3. CD to the directory SSH-Login-Monitor is in.
4. Run `python -m venv .venv`
5. **Activate the venv:** <br> For Unix or MacOS: `source .venv/bin/activate` <br> For Windows: `.venv\bin\activate`
6. Install required dependencies with `pip install -r requirements.txt`

**To run:**

1. Open your terminal.
2. CD to the directory this program is saved in.
3. Run the command `python main.py` or you can run it with the file in it's directory.

**Disclaimer**: You may have to install all the dependencies if not installed by the setup.

_**To configure the private key simply edit the config file and include the path to where your ssh key is located.**_
