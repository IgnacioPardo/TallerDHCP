import socket
from sys import argv

if __name__ == '__main__':

    if len(argv) != 2 or argv[1][0] != '-' or len(argv[1]) > 4*4:
        print('Modo de uso:\n python checkIP.py -{IP a chequear} -{mensaje}')
        quit()

    host = argv[1][1:] # IP del host
    port = 10000 # numero de puerto
    msg = argv[2][1:]

    sock = socket.socket(socket.AF_INET, # Internet
                socket.SOCK_DGRAM) # UDP
                
    sock.sendto(msg.encode(), (host, port))

    data = sock.recv(1024).decode() # escuchamos la respuesta
    print('El paquete recibido fue: \n' + data)
    sock.close()