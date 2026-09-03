from cliente_pb2 import Cliente
cliente = Cliente()

cliente.id = 1
cliente.nombre = "Bray"
cliente.mail = "bray@email.com"
cliente.telefono = "3001234567"
cliente.tipo_id = 1
cliente.genero_id = 1
print(cliente)
print("Cliente tipo: ",type(cliente))

datos_serializados = cliente.SerializeToString()

print("\nDatos serializados: ",datos_serializados)
print(type(datos_serializados))
print("Tamaño:", len(datos_serializados), "bytes")

cliente_reconstruido = Cliente()
cliente_reconstruido.ParseFromString(datos_serializados)

print("\nDatos deserializados:\n",cliente_reconstruido)
print("Cliente_reconstruido tipo: ",type(cliente_reconstruido))