import socket
import json
import requests
import time

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

    print("____________________________________________________________________\n")
    print("\nCLIENTE API")
    print(cliente_api);
    print(respuesta.status_code)
    print("Tipo: ", type(cliente_api))

    inicio_tiempo = time.perf_counter()

    cliente_json = json.dumps(cliente_api)

    fin_tiempo = time.perf_counter()
    tiempo = fin_tiempo - inicio_tiempo

    tamano = len(cliente_json.encode("utf-8"))

   
    print("\nCLIENTE JSON")
    print(cliente_json)
    print("Tipo: ", type(cliente_json))
    print("Tamaño:", tamano, "bytes")
    print("Tiempo de serialización:", tiempo, "segundos\n")


    conexion.send(cliente_json.encode())


conexion.close()
servidor.close()




  
        
    

