# Imports
from os import system
from random import seed, randint
from paramiko import SSHClient, AutoAddPolicy 
from paramiko.auth_handler import AuthenticationException, SSHException
from scp import SCPClient, SCPException

def main():
    #verificar se o arquivo ssh existe
    #copiar arquivo
    #enviar pra maquina remota
    #inciar processo de copia usando scp
    commands = [
        "mkdir ~/uploads"
    ]
    
    filepaths = [
        "C:/Users/maria/Downloads/teste"
    ]

    local_file_directory = "C:/Users/maria/Downloads/teste"
    remote_path = "~/uploads"
    ssh_key_filepath = "~/.ssh/id_rsa.pub"

    host = "127.0.0.1"
    user = "maria"
    password = ""
    
    # ssh_key = RSAKey.from_private_key_file(ssh_key_filepath)
    # system(f"ssh-copy-id -i {ssh_key_filepath}.pub {user}@{host}>/dev/null 2>&1")
    
    try:
        client = SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(
            host,
            username=user,
            password=password,
            key_filename=ssh_key_filepath,
            timeout=5000,
        )
        return client
    except AuthenticationException as e:
        print("Erro AuthenticationException a chave SSH foi gerada? " + str(e))
    except Exception as e:
        print("Erro: " + str(e))

    for cmd in commands:
        stdin, stdout, stderr = client.exec_command(cmd)
        stdout.channel.recv_exit_status()
        response = stdout.readlines()
        for line in response:
            print("INPUT: {cmd}\n \ OUTPUT: {line}")

    scp = SCPClient(client.get_transport())
    
    try:
        scp.put(
            local_file_directory,
            remote_path=remote_path,
            recursive=True
        )
        print("Finished uploading "+ len(filepaths) + " files to " + {remote_path} + " on " + {host})
    except SCPException as e:
        print("SCPException during bulk upload: " + str(e))
    except Exception as e:
        print("Unexpected exception during bulk upload: " + str(e))
    
    if client:
        client.close()
    if scp:
        scp.close()

if __name__ == "__main__":
    main()