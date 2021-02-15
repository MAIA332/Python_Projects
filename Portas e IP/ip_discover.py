import os,time
import pandas as pd
import socket, threading, platform
from scan import _scn_

def get_data(host,port):
    try:
        print('get_data')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((host,port))
        dados = s.recv(1024)

        print(dados.decode('ascii'))
        s.close()

    except Exception as e:
        print(f'Erro: {e}')
        return False

def open_port(host,port):
    print('open_port')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:           
        
        msg = 'Porta aberta'

        s.bind((host,port))
        print('Listen...')
        s.listen(5)

        while True:
            c,e = s.accept()
            print('conected with',e)
            c.send(msg.encode('ascii'))
            c.close()
            break
            

    except Exception as e:
        print(f'Erro: {e}')
        return False
    

def ping(host):

    if  platform.system().lower()=="windows":
        ping_str = "-n 1"
    else:
        ping_str = "-c 1"

    resposta = os.system("ping " + ping_str + " " + host)
    return resposta ==0

                       
def armazenar_arp():
    
    validation = os.popen("arp -a").read()
    validation = validation.split('\n')
    validation = validation[3:]
    validation = str(validation).strip('[]')
    validation = validation.split(' ')
    _val_ = []

    for i in validation:
        if(i!='')and (i!="'")and(i!="',")and(i!="''"):
            _val_.append(i)

    nval_ = []

    for i in _val_:
        if not (i.find('192.')):
            nval_.append(i)

    return nval_

def validate_active_ip(ip_strip):
    validated_ip = []

    for i in ip_strip:
        resposta = ping(i)

        if(resposta == True):
            validated_ip.append(i)
        else:
            pass
    
    return validated_ip

def build_console(frame_strips):

    time.sleep(1)
    os.system('cls')
    print("=================================================================")
    print("=================================================================")
    print(frame_strips)
    print("=================================================================")
    print("=================================================================")
    os.system('pause')
    build_menu()

def ini():
    host = input('Digite o IPV4 alvo: ')
    port = int(input('Porta alvo: '))

    try:
        t1 = threading.Thread(target = open_port, args=(host,port))
        t2 = threading.Thread(target = get_data, args=(host,port))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("Successed!")
        os.system('pause')

    except:
        print(f'Não foi possivel se conectar à {host}. Possivel erro no processamento paralelo')

def build_menu():
    os.system('cls')
    print("==============================================================")
    print("============================================================== \n")
    print(" (1) IP Scan  \n (2) PORT Scan  \n (3) Pen testing (beta) ")
    print("\n==============================================================")
    print("==============================================================")


def IP_scan():
    os.system('cls')
    my_ip = input('IPV4: ')

    s = armazenar_arp()
    s.append(my_ip)

    active_strip = validate_active_ip(s)

    dict_ = {'All':s,'Active':active_strip}
    frame_strips = pd.DataFrame.from_dict(dict_,orient='index')
    frame_strips = frame_strips.transpose()

    build_console(frame_strips)


def Main_build():
   
    _scan_ = _scn_.scan()

    while True:
        build_menu()
        _exec_ = int(input('Execução: '))
        if _exec_ == 1:
            IP_scan()
            
        elif _exec_ ==2:
            _scan_.Main()

        elif _exec_ == 3:
            ini()

Main_build()
