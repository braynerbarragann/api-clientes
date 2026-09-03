import json
import socket
import time

#print(type(cliente_json))

cliente_socket = socket.socket()
cliente_socket.connect(("localhost", 8001))

while True:
    mensaje = input("Ingrese del cliente: ")
    # Si el cliente no envía nada o escribe 'salir', rompemos el bucle
    if not mensaje.isnumeric():
        print("\nSe cerró la comunicación.")
        break

    cliente_id = mensaje

    cliente_socket.send(cliente_id.encode())

    respuesta_server = cliente_socket.recv(1024).decode()
    tamano = len(respuesta_server.encode("utf-8"))

    print("____________________________________________________________________\n")
    print("\nRespuesta servidor:", repr(respuesta_server))
    print("Tipo: ", type(respuesta_server))
    print("Tamaño:", tamano, "bytes")

    inicio_tiempo = time.perf_counter()

    cliente_obj = json.loads(respuesta_server)

    fin_tiempo = time.perf_counter()
    tiempo = fin_tiempo - inicio_tiempo

    
    
    print("\nObjeto reconstruido:", cliente_obj)
    print("Tipo: ", type(cliente_obj))
    print("Tiempo deserialización:", tiempo, "segundos\n")
    
    
cliente_socket.close()



