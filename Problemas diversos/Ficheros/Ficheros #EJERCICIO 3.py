n = int(input("Ingrese un nro del 1 al 10: "))
m = int(input("Introduce otro número entero entre 1 y 10: "))
file = f"./tabla-{n}.txt"
try: 
    f = open(file, "r")
except FileNotFoundError:
    print("No existe el fichero con la tabla del ", n)
else:
    lines = f.readlines()
    print(lines[m - 1])