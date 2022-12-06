# Imports
from os import system, getenv
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
        "~/Downloads/teste"
    ]

    local_file_directory = getenv("local_file_directory")
    remote_path = getenv("remote_path")
    ssh_key_filepath = getenv("ssh_key_filepath")

    host = getenv("host")
    user = getenv("user")
    password = getenv("password")
    
    system(f"ssh-copy-id -i {ssh_key_filepath}.pub {user}@{host}:~/.ssh/authorized_keys")
    
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
        print("Backup finalizado "+ len(filepaths) + " arquivos para " + {remote_path} + " em " + {host})
    except SCPException as e:
        print("SCPException: " + str(e))
    except Exception as e:
        print("Erro: " + str(e))
    
    if client:
        client.close()
    if scp:
        scp.close()

if __name__ == "__main__":
    main()