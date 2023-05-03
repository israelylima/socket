# Sockets

Segundo Kurose, sockets são uma das principais abstrações usadas para programar aplicações de rede. Eles permitem que processos em diferentes computadores se comuniquem entre si através da rede, usando diferentes protocolos de transporte, como TCP e UDP.

## Linguagem de programação

Para o desenvolvimento do trabaho utilizamos a linguagem Python. Por ser uma linguagem conhecida entre as membras da equipe, a linguagem também permite a fácil utilização devido suas bibliotecas. 

## Bibliotecas

**• socket:** Para criação de sockets 

**• random:** Para gerar números aleatórios

**• time:** Trabalha com a medida de tempo 

## Dicionário: 
```
socket.AF_INET
```
- Endereços usada pelo socket, nesse caso o endereço é do tipo IPv4. 

```
socket.SOCK_STREAM
```
- Tipo de socket a ser usado, nesse caso um socket de fluxo (que implementa o TCP). 

```
server_socket.bind
```
- Associa o socket a um endereço IP e porta específicos.

```
server_socket.listen
```
- Coloca o servidor em modo de espera para receber conexões de clientes. O método é usado depois de chamar a função "bind()" para configurar. 

```
server_socket.accept()
```
- O objeto socket aceita uma conexão de um cliente.

```
client_socket.send
```
- É usado para enviar dados do servidor para o cliente.

```
client_socket.recv
```
- Usado para receber dados do cliente para o servidor.

```
client_socket.close()
```
- Fecha a conexão de um socket.


## Funcionamento

**• Servidor:** 
É criado um socket utilizando TCP, depois de atribuir a porta e servidor. Depois de configurar o socket do servidor com as funções "bind()" e "listen()", o servidor fica aguardando conexões de clientes. Quando um cliente tenta se conectar, o servidor aceita a conexão usando a função "accept()", criando um novo socket para lidar com a comunicação com aquele cliente específico. Enquanto existir uma conexão, o servidor executa suas verificações, no nosso caso, se o número recebido do cliente é par, ímpar ou se tem mais de 10 digitos. 

**• Cliente:** 
O mesmo acontece com o cliente, um socket é criado e ele tenta se conectar com o servidor. Mas, diferente do servidor, o cliente gera um número aleatório, envia para o servidor e recebe sua resposta que é imprimida no console juntamente com a palavra "FIM". 


## Como executar 

01. Depois de baixar os dois arquivos, execute no prompt de comando ou na sua IDE o arquivo servidor.py
02. Em seguida, execute no prompt de comando ou na sua IDE o arquivo cliente.py

## Autores

- [@israelylima](https://github.com/israelylima)
- Suellen Correia
