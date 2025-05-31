

def ingresar_notas() -> list[float]:
    n = input("Ingrese sus notas: ")
    n = n.split(" ")
    notas = [float(nota) for nota in n]
    print(notas)