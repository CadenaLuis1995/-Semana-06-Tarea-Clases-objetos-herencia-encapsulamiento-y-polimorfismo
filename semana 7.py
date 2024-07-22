class Producto:
    """
    Clase que representa un producto con nombre, precio y cantidad.

    Atributos:
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        cantidad (int): Cantidad del producto en stock.

    Métodos:
        __init__(self, nombre, precio, cantidad): Constructor para inicializar los atributos del producto.
        __del__(self): Destructor para imprimir un mensaje al eliminar el objeto.
        mostrar_informacion(self): Muestra la información del producto (nombre, precio, cantidad).
    """

    def __init__(self, nombre, precio, cantidad):
        """
        Constructor para inicializar los atributos del producto.

        Argumentos:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            cantidad (int): Cantidad del producto en stock.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

        print(f"Producto '{self.nombre}' creado con precio {self.precio:.2f} y cantidad {self.cantidad}")

    def __del__(self):
        """
        Destructor para imprimir un mensaje al eliminar el objeto.

        Se activa cuando el objeto se elimina de la memoria o se sale del alcance.
        """
        print(f"Producto '{self.nombre}' eliminado.")

    def mostrar_informacion(self):
        """
        Muestra la información del producto (nombre, precio, cantidad).
        """
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio:.2f}")
        print(f"Cantidad: {self.cantidad}")


# Ejemplo de uso

producto1 = Producto("Laptop", 800.00, 10)
producto1.mostrar_informacion()

# Simulamos la eliminación del objeto

del producto1

# Se activa el destructor
