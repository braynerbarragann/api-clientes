import socket
import requests
import time
from cliente_pb2 import Cliente


#Configurar y encender el servidor
servidor = socket.socket()
servidor.bind(('localhost', 8001))
servidor.listen(1)
print("Servidor esperando.................")

 
# Aceptar al cliente cuando llegue
conexion, direccion = servidor.accept()

while True:
    mensaje = conexion.recv(1024).decode()
    # Si el cliente no envía nada o escribe 'salir', rompemos el bucle
    if not mensaje.isnumeric():
        print("\nSe cerró la comunicación.")
        break

    respuesta = requests.get(f'http://127.0.0.1:8000/clientes/{mensaje}')
    cliente_api = respuesta.json()

    if respuesta.status_code != 200:
        print("Error:", cliente_api)
        conexion.sendall(b"ERROR: Cliente no encontrado")
        continue

    

    print("____________________________________________________________________\n")
    print("\nCLIENTE API")
    print(cliente_api);
    print(respuesta.status_code)
    print("Tipo: ", type(cliente_api))

    cliente_proto = Cliente()

    cliente_proto.id = cliente_api["id"]
    cliente_proto.nombre = cliente_api["nombre"]
    cliente_proto.mail = cliente_api["mail"]
    cliente_proto.telefono = cliente_api["telefono"]
    cliente_proto.tipo_id = cliente_api["tipo_id"]
    cliente_proto.genero_id = cliente_api["genero_id"]

    inicio_tiempo = time.perf_counter()

    datos_serializados = cliente_proto.SerializeToString()

    fin_tiempo = time.perf_counter()
    tiempo = fin_tiempo - inicio_tiempo

    tamano = len(datos_serializados)

   
    print("\nCLIENTE BYTES")
    print(datos_serializados)
    print("Tipo: ", type(datos_serializados))
    print("Tamaño:", tamano, "bytes")
    print("Tiempo de serialización:", tiempo, "segundos\n")


    conexion.sendall(datos_serializados)


conexion.close()
servidor.close()




  
        
    

