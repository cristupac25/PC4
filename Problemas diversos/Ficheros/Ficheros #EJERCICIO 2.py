n = int(input("Ingrese un nro del 1 al 10: "))
file = f"./tabla-{n}.txt"
try: 
    f = open(file, "r")
except FileNotFoundError:
    print("No existe el fichero con la tabla del", n)
else:
    print(f.read())
