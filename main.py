import yaml, paramiko, getpass, traceback, time, itertools
from paramiko_expect import SSHClientInteraction

with open("config.yaml", "r") as yamlfile:
    cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)

def main():

    command = "sudo tail -f /var/log/auth.log"

    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        server_pw = getpass.getpass("Enter the password for your account %s on %s:" % (cfg['ssh_config']['username'], cfg['ssh_config']['host']))
        sudo_pw = getpass.getpass("Enter the sudo password for %s on %s: " % (cfg['ssh_config']['username'], cfg['ssh_config']['host']))
        ssh.connect(hostname = cfg['ssh_config']['host'], username = cfg['ssh_config']['username'], port = cfg['ssh_config']['port'], password = server_pw)

        interact = SSHClientInteraction(ssh, timeout=10, display=False)
        interact.send(command)
        interact.send(sudo_pw + "\n")

        with open(interact.tail(line_prefix=cfg['ssh_config']['servername']+': ')) as tail:
            for line in itertools.islice(tail, 17, None):
                print(line)

    except KeyboardInterrupt:
            print('Ctrl+C interruption detected, stopping tail')
    except Exception:
        traceback.print_exc()
    finally:
        try:
            ssh.close()
        except:
            pass

if __name__ == '__main__':
       main()