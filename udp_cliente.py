import socket

host = "" # IP del host
port = 10000 # numero de puerto
msg = "Hello, World!"

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
             
sock.sendto(msg.encode(), (host, port))

data = sock.recv(1024).decode() # escuchamos la respuesta
print('El paquete recibido fue: \n' + data)
sock.close()