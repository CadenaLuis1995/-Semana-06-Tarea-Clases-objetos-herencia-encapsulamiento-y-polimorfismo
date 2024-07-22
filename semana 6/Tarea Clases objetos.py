# Definición de la clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print("El animal está comiendo.")

# Definición de la clase derivada
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        print("El perro está ladrando.")

    # Ejemplo de polimorfismo mediante un método sobrescrito
    def comer(self):
        print("El perro está comiendo croquetas.")

# Creación de instancias de las clases
animal_generico = Animal("Animal Genérico")
perro = Perro("Firulais", "Labrador")

# Acceso a atributos y métodos de las clases
print(animal_generico.nombre)
animal_generico.comer()

print(perro.nombre)
print(perro.raza)
perro.comer()
perro.ladrar()
