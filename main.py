from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():
    # Crear el restaurante
    restaurante = Restaurante("Sazón Manabí")

    # Crear los platillos
    platillo_1 = Platillo(
        "Camaron apanado",
        6.50,
        True,
        "Plato típico",
        10
    )

    platillo_2 = Platillo(
        "Sopa de bagre",
        3.75,
        True,
        "Almuerzo",
        12
    )

    # Crear las bebidas
    bebida_1 = Bebida(
        "Agua de coco",
        1.00,
        True,
        500,
        "Natural"
    )

    bebida_2 = Bebida(
        "Coca cola",
        1.75,
        True,
        1000,
        "Botella"
    )

    # Modificar el precio utilizando encapsulación
    platillo_1.cambiar_precio(7.00)

    # Agregar todos los productos al restaurante
    restaurante.agregar_producto(platillo_1)
    restaurante.agregar_producto(platillo_2)
    restaurante.agregar_producto(bebida_1)
    restaurante.agregar_producto(bebida_2)

    # Mostrar los productos registrados (Polimorfismo)
    restaurante.mostrar_productos()


# Punto de inicio del programa
if __name__ == "__main__":
    main()