# Restaurante App - Sistema de Gestión de Productos

## Nombre del estudiante

Dennis Gilson Betancourt Yanacallo

## Descripción del sistema

Este proyecto consiste en el desarrollo de un sistema básico para la gestión de productos de un restaurante utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite registrar platillos y bebidas, almacenarlos en una lista administrada por el restaurante y mostrar la información de cada producto de manera organizada mediante una estructura modular.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Relación de herencia

La clase **Producto** representa la clase padre del sistema, ya que contiene los atributos y métodos comunes para todos los productos del restaurante.

A partir de esta clase se derivan las clases **Platillo** y **Bebida**, las cuales heredan sus características generales y agregan atributos propios según el tipo de producto.

## Encapsulación

El atributo **precio** fue encapsulado utilizando `__precio`, impidiendo que sea modificado directamente desde otras clases.

Para acceder o modificar su valor se utilizan los métodos:

- `obtener_precio()`
- `cambiar_precio()`

Además, el método `cambiar_precio()` valida que el nuevo precio sea mayor que cero antes de realizar la modificación.

## Polimorfismo

El método `mostrar_informacion()` fue sobrescrito en las clases **Platillo** y **Bebida**.

Gracias al polimorfismo, la clase `Restaurante` puede recorrer una lista de productos y ejecutar el mismo método para todos los objetos, obteniendo una salida diferente según el tipo de producto.


