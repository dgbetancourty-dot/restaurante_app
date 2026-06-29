class Restaurante:
    # Constructor de la clase Restaurante
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    # Agrega un producto a la lista del restaurante
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Muestra todos los productos registrados
    def mostrar_productos(self):
        print(f"\n===== PRODUCTOS DEL RESTAURANTE {self.nombre.upper()} =====")

        for producto in self.productos:
            print(producto.mostrar_informacion())