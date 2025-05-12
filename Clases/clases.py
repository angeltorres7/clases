class armas:
    def __init__(self, cañon, culata, cargador, mira, empuñadura):
       self.cañon = cañon
       self.culata = culata
       self.cargador = cargador
       self.mira = mira
       self.empuñadura = empuñadura
       
ladra = armas ("reforzado", "pesada", "ampliado 1", "mira opv4", "desenfundado rapido")
print(ladra.cañon)
print(ladra.empuñadura)