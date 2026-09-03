import socket
import time
from cliente_pb2 import Cliente


#print(type(cliente_json))

cliente_socket = socket.socket()
cliente_socket.connect(("localhost", 8001))

while True:
    mensaje = input("Ingrese id del cliente: ")
    # Si el cliente no envía nada o escribe 'salir', rompemos el bucle
    if not mensaje.isnumeric():
        print("\nSe cerró la comunicación.")
        break

    cliente_id = mensaje

    cliente_socket.send(cliente_id.encode())

    respuesta_server = cliente_socket.recv(1024)
    if respuesta_server.startswith(b"ERROR"):
        print(respuesta_server.decode())
        continue

    tamano = len(respuesta_server)


    print("____________________________________________________________________\n")
    print("\nRespuesta servidor:", repr(respuesta_server))
    print("Tipo: ", type(respuesta_server))
    print("Tamaño:", tamano, "bytes")

    cliente_reconstruido = Cliente()
    
    inicio_tiempo = time.perf_counter()

    cliente_reconstruido.ParseFromString(respuesta_server)

    fin_tiempo = time.perf_counter()
    tiempo = fin_tiempo - inicio_tiempo

    
    
    print("\nObjeto reconstruido:", cliente_reconstruido)
    print("Tipo: ", type(cliente_reconstruido))
    print("Tiempo deserialización:", tiempo, "segundos\n")
    
    
cliente_socket.close()



