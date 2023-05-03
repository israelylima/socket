#Trabalho de redes • Israely Lima e Suellen Correia
import socket
import random
import time

# Endereço e porta do servidor
HOST = 'localhost'
PORT = 60000

while True:
    # Cria o socket do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor
    client_socket.connect((HOST, PORT))

    # Gera um número aleatório com até 30 dígitos
    num = random.randrange(10**29, 10**30)
    
    # Envia o número para o servidor
    client_socket.send(str(num).encode())

    # Recebe a resposta do servidor
    data = client_socket.recv(1024).decode()

    # Imprime a resposta 
    print(data)
    print(f"FIM -")

    # Espera 10 segundos antes de repetir o processo
    time.sleep(10)
    client_socket.close()




