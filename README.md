# backup-ssh
Para executar este projeto deve-se primeiro gerar uma chave ssh na máquina que irá receber os arquivos de backup,
usando o comando:

```
ssh-keygen -t rsa
```

Faça uma cópia do arquivo .env, e preencha os valores das constantes de acordo.

Referência: https://hackersandslackers.com/automate-ssh-scp-python-paramiko/