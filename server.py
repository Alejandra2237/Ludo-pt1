#Permite intercambiar inf entre procesos en la misma máquina o en una red
#Distribuye el trabajo a la máquina más eficieinte y permiten facilmente acceso a datos centralizados
import socket 
#Subproceso que permite ejecutar funciones en paralelo
from  threading import Thread

#Declaramos variables globales sin ningún valor por el momento
SERVER = None
PORT = None
IP_ADDRESS = None

#Declaramos un diccionario de clientes vacío
CLIENTS = {}




def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()

        





#Creación del servidor
def setup():
    print("\n")
    print("\t\t\t\t\t\t*** ESCALERA LUDO ***")


    global SERVER
    global PORT
    global IP_ADDRESS

    #El puerto pueden ser cualquier número solo que nos sea inferior a 1024
    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    #Conectamos nuestro servidor con la IP y puerto que estamos usando
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #La función bind() toma una tupla con dirección IP y puerto
    SERVER.bind((IP_ADDRESS, PORT))
    #Podemos escuchar en el sockect de servidor 10 conexiones
    SERVER.listen(10)

    print("\t\t\t\tEL SERVIDOR ESTÁ ESPERANDO CONEXIONES ENTRANTES...")
    print("\n")

    acceptConnections()


setup()
