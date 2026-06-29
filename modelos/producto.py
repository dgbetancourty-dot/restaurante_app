class Producto:
    # Constructor de la clase padre
    def __init__(self, nombre, precio, disponibilidad=True):
        self.nombre = nombre
        self.__precio = precio
        self.disponibilidad = disponibilidad

    # Permite obtener el precio del producto
    def obtener_precio(self):
        return self.__precio

    # Permite modificar el precio validando que sea correcto
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            print("Error: el precio debe ser mayor a cero.")
        else:
            self.__precio = nuevo_precio

    # Indica si el producto está disponible
    def esta_disponible(self):
        return self.disponibilidad

    # Muestra la información básica del producto
    def mostrar_informacion(self):
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f}"