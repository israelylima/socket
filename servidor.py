#Trabalho de redes • Israely Lima e Suellen Correia
import socket

# Endereço e porta do servidor
HOST = 'localhost'
PORT = 60000

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind do socket do servidor com o endereço e porta definidos
server_socket.bind((HOST, PORT))

# Espera por conexões de clientes
server_socket.listen()

while True:
    # Aguarda a conexão de um cliente
    print('Aguardando conexão de um cliente...')
    client_socket, addr = server_socket.accept()
    print(f'Cliente {addr} conectado!')

    # Recebe o número enviado pelo cliente
    data = client_socket.recv(1024).decode('utf-8')



    # Verifica se o número tem mais de 10 dígitos
    if len(data) > 10:
        # Gera uma string aleatória com o mesmo tamanho do número e envia para o cliente
        string_aleatoria = '-'.join([str(i) for i in range(len(data))])
        client_socket.send(string_aleatoria.encode('utf-8'))
    else:
        # Verifica se o número é par ou ímpar e envia a resposta para o cliente
        if int(data) % 2 == 0:
            client_socket.send(' PAR '.encode('utf-8'))
        else:
            client_socket.send(' ÍMPAR '.encode('utf-8'))

    # Fecha a conexão com o cliente
    client_socket.close()
