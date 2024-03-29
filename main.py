#                     GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007
#                       
# SSH Login Monitor - Monitors your login info on linux sever.
# Copyright (C) 2021 - vapouryh
#
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

import yaml, paramiko, getpass, time, threading
from paramiko_expect import SSHClientInteraction

threading.TIMEOUT_MAX = 4294967.0

with open("config.yaml", "r") as yamlfile:
    cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)

def main():

    command = "sudo tail -f /var/log/auth.log"

    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        server_pw = getpass.getpass("Enter the password for your account %s on %s:" % (cfg['ssh_config']['username'], cfg['ssh_config']['host']))
        try: 
            ssh.connect(hostname = cfg['ssh_config']['host'], username = cfg['ssh_config']['username'], port = cfg['ssh_config']['port'], password = server_pw, key_filename= cfg['ssh_config']['key_path'])
        except TimeoutError:
            print("Operation timed out. Check password and/or try again.")
            exit()

        stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)

        time.sleep(2)
        stdin.write(server_pw + "\n")
        stdin.flush()

        for line in iter(stdout.readline, ""):
            print(line, end="")

    except KeyboardInterrupt:
        print('Ctrl+C interruption detected, stopping tail')
    finally:
        try:
            ssh.close()
        except:
            pass

if __name__ == '__main__':
    main()
