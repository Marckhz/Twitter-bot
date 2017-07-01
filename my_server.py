import socket

#create a tcp/ip socket

sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket
server_addr = ('192.168.0.4', 5003)
print ('el socket comenzo en la direccion %s en el puerto %s \n' % server_addr)
sock.bind(server_addr)


sock.listen(3)
while True:
    #wConectando...
    print "esperando a conectar"
    conn, client_adrr = sock.accept()

    try:
        print 'en linea desde ', client_adrr

        while True:
            data = conn.recv(16)
            print "recibido... %s \n" %data


    finally:
        conn.close()
