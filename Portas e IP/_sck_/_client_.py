import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.15.15'
port = 80

s.connect((host,port))
dados = s.recv(1024)

print(dados.decode('ascii'))