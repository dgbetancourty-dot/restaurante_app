from modelos.producto import Producto


class Bebida(Producto):
    # Constructor de la clase hija Bebida
    def __init__(self, nombre, precio, disponibilidad, volumen_ml, tipo_bebida):
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida

    # Sobrescribe el método de la clase padre (Polimorfismo)
    def mostrar_informacion(self):
        estado = "Disponible" if self.esta_disponible() else "No disponible"

        return (
            f"Bebida: {self.nombre} | "
            f"Tipo: {self.tipo_bebida} | "
            f"Volumen: {self.volumen_ml} ml | "
            f"Precio: ${self.obtener_precio():.2f} | "
            f"Estado: {estado}"
        )