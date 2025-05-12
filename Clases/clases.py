#primero creamos un clase
class armas:
    def __init__(self, cañon, culata, cargador, mira, empuñadura):#Definimos los atributos
       #Ponemos los atributos con el self
       self.cañon = cañon
       self.culata = culata
       self.cargador = cargador
       self.mira = mira
       self.empuñadura = empuñadura

#Completamos el codigo
ladra = armas ("reforzado", "pesada", "ampliado 1", "mira opv4", "desenfundado rapido")
print(ladra.cañon)
print(ladra.empuñadura)
#En programación, una clase es una plantilla o modelo para crear objetos. Define las características (atributos) y el comportamiento (métodos) que tendrán los objetos creados a partir de esa clase. Es un concepto fundamental en la programación orientada a objetos 

#Torres Perez Roberto Angel
