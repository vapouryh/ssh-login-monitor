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
        ssh.connect(hostname = cfg['ssh_config']['host'], username = cfg['ssh_config']['username'], port = cfg['ssh_config']['port'], password = server_pw)

        interact = SSHClientInteraction(ssh, display=False)
        interact.send(command)
        time.sleep(2)
        interact.send(server_pw + "\n")
        time.sleep(2)

        with open(interact.tail(line_prefix=cfg['ssh_config']['servername']+': ', timeout=threading.TIMEOUT_MAX)) as tail:
            for line in tail:
                print(line)

    except KeyboardInterrupt:
        print('Ctrl+C interruption detected, stopping tail')
    finally:
        try:
            ssh.close()
        except:
            pass

if __name__ == '__main__':
    main()