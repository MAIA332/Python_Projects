import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#protocolo IPv4 e UDP

host = '192.168.15.15'
port = 80
msg = 'Eae cliente'

s.bind((host,port))
s.listen(1)

while True:
    c,e = s.accept()
    print('conected with',e)
    c.send(msg.encode('ascii'))
    c.close()