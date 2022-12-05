# Imports
from os import system
from random import seed, randint
from paramiko import RSAKey, SSHClient, AutoAddPolicy

class Processo:
    def __init__(self, qtdPag):
        seed()
        self.id = randint(1000, 9999)
        self.qtdPag = qtdPag

def main():
    #verificar se o arquivo ssh existe
    #copiar arquivo
    #enviar pra maquina remota
    #inciar processo de copia usando scp

    localfilepath = ""
    remotefilepath = ""
    ssh_key_filepath = ""

    hostnameInput = "host"
    usernameInput = "user"
    passwordInput = "password"
    host = ""
    user = ""

    ssh_key = RSAKey.from_private_key_file(ssh_key_filepath)
    system(f"ssh-copy-id -i {ssh_key_filepath}.pub {user}@{host}>/dev/null 2>&1")

    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    ssh_client.connect(hostname = hostnameInput, username = usernameInput, password = passwordInput)

    ftp_client = ssh_client.open_sftp()
    ftp_client.put(localfilepath, remotefilepath)
    ftp_client.close()

if __name__ == "__main__":
    main()