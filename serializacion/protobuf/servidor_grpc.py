import grpc
from concurrent import futures
import cliente_pb2
import cliente_pb2_grpc
import requests


class ClienteService(cliente_pb2_grpc.ClienteServiceServicer):


    def ObtenerCliente(self, request, context):
        print("Solicitud recibida")
        print("ID:", request.id)
    
        respuesta = requests.get(
            f"http://127.0.0.1:8000/clientes/{request.id}"
        )
    
        if respuesta.status_code != 200:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Cliente no encontrado\n")
            return cliente_pb2.Cliente()
    
        cliente_api = respuesta.json()
    
        cliente = cliente_pb2.Cliente()
        cliente.id = cliente_api["id"]
        cliente.nombre = cliente_api["nombre"]
        cliente.mail = cliente_api["mail"]
        cliente.telefono = cliente_api["telefono"]
        cliente.tipo_id = cliente_api["tipo_id"]
        cliente.genero_id = cliente_api["genero_id"]
    
        return cliente


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#registra el servicio
cliente_pb2_grpc.add_ClienteServiceServicer_to_server(
    ClienteService(),
    servidor
)

servidor.add_insecure_port("[::]:50051")

servidor.start()

print("Servidor gRPC iniciado en el puerto 50051")

servidor.wait_for_termination()