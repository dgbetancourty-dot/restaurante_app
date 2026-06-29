from modelos.producto import Producto


class Platillo(Producto):
    # Constructor de la clase hija Platillo
    def __init__(self, nombre, precio, disponibilidad, tipo_platillo, tiempo_preparacion):
        super().__init__(nombre, precio, disponibilidad)
        self.tipo_platillo = tipo_platillo
        self.tiempo_preparacion = tiempo_preparacion

    # Sobrescribe el método de la clase padre (Polimorfismo)
    def mostrar_informacion(self):
        estado = "Disponible" if self.esta_disponible() else "No disponible"

        return (
            f"Platillo: {self.nombre} | "
            f"Tipo: {self.tipo_platillo} | "
            f"Tiempo de preparación: {self.tiempo_preparacion} min | "
            f"Precio: ${self.obtener_precio():.2f} | "
            f"Estado: {estado}"
        )