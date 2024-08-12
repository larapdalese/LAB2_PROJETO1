def cumprimento(texto):
    return (f"Olá, {texto}!")
print(cumprimento("Lara Peclart Dalese"))

import random
def sorteio():
     numeros = [random.randint(0, 10) for _ in range(3)]
     print(numeros)
     media = sum(numeros) / len(numeros)
     return media
print(sorteio())
