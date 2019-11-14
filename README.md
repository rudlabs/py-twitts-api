# py-twitts-api
Aplicação Web para obter o Twitter baseado em hashtag e criar uma lista dos usuários com mais seguidores.

## Aplicação, Logs e Monitoração:
Atenção: 
  Para iniciar a aplicação é necesséario subir primeiro a stack de logs devido a dependência da aplicação!

1) Dentro do diretório /logging, execute o comando abaixo do docker compose para iniciar a stack:
```bash
$ docker-compose up -d
```
2) Agora execute o mesmo comando dentro do diretório /app e em seguida no /monit.

3) Execute o comando abaixo para certificar-se de que os containers estão em execução:
```bash
$ docker ps -a
```
4) Para derrubar os containers via docker compose basta executar o comando abaixo dentro do diretório de cada stack:
```bash
$ docker-compose down
```
ou se desejar derrubar todos de uma vez:
```bash
$ docker ps -a | awk '{print $1}' | egrep -iv container | xargs docker rm -f
```
