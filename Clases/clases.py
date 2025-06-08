# Clase base Figura con un método area que se espera que sea sobreescrito por las subclases
class Figura:
    def area(self):
        return()  # Método base sin implementación real

# Clase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio  # Se guarda el radio del círculo
    def area(self):
        # Fórmula del área de un círculo: π * radio^2 (usando 3.14 como valor aproximado de π)
        return 3.14 * self.radio ** 2

# Clase Rectangulo que hereda de Figura
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base      # Se guarda la base del rectángulo
        self.altura = altura  # Se guarda la altura del rectángulo
    def area(self):
        # Fórmula del área de un rectángulo: base * altura
        return self.base * self.altura

# Lista de figuras: un círculo y un rectángulo
figuras = [Circulo(30), Rectangulo(15, 10)]

# Se recorre la lista y se imprime el área de cada figura
for figura in figuras:
    print(f"El área de la figura es {figura.area()}")


#Torres Pérez Roberto Angel 