import socket

#create a tcp/ip socket

sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket
server_addr = ('xxx.xxx.x.x', 5003)
print ('el socket comenzo en la direccion %s en el puerto %s \n' % server_addr)
sock.bind(server_addr)
sock.listen(3)

def runTime():

    print  'iniciando operacion'
    time.sleep(5)
    print "cafe! listo!"

def socketRun():
        while True:
                print "esperando a conectar"
                conn, client_adrr = sock.accept()
                try:
                    print 'en linea desde \n', client_adrr
                    while True:
                        data = conn.recv(4016)

                        print "recibido... %s \n" %data
                        usr = data
                        str1 = 'Master'
                        if  data == str1:
                            str1.find(usr)
                            tr = threading.Thread(runTime())
                            tr.start()
                            conn.send('Estamos preparando el cafe!\n')
                        else:
                            print 'nel prro'
                finally:
                        conn.close()

if __name__ == '__main__':
     socketRun();
