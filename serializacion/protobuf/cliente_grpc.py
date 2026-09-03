import grpc

import cliente_pb2
import cliente_pb2_grpc


canal = grpc.insecure_channel("localhost:50051")

stub = cliente_pb2_grpc.ClienteServiceStub(canal)

while True:

    mensaje = input("Ingrese id del cliente: ")

    if not mensaje.isnumeric():
        print("\nSe cerró la comunicación.")
        break

    request = cliente_pb2.ClienteRequest(
        id=int(mensaje)
    )

    try:
        respuesta = stub.ObtenerCliente(request)

        print("____________________________________________")
        print("\nRespuesta servidor:")
        print(respuesta)
        print("Tipo:", type(respuesta))

    except grpc.RpcError as e:
        print("____________________________________________")
        print("\nError:", e.code())
        print("Detalle:", e.details())

canal.close()

