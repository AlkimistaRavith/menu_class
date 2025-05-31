import sys
from notas.menu import menu

def main ():
    notas = []

    while True:
        menu()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
           

        elif opcion == 2:
            try:
                promedio = sum(notas) / len(notas)
                mayor = max(notas)
                menor = min(notas)
                aprobados = [a for a in notas if a >= 4.0]
            except ZeroDivisionError:
                print("\nFalta agregar notas (Seleccione opción 1)")
                
        elif opcion == 3:
            print(f"""
Promedio: {promedio:.1f}
Nota mayor: {mayor}
Nota menor: {menor}
Notas aprobadas: {aprobados}
""")
        elif opcion == 4:
            print(4)
            break
        else:
            print("fin")
            break

if __name__ == "__main__":
    main()