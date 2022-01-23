n = int(input("Ingrese un numero del 1 al 10: "))
file = f"./tabla-{n}.txt"
with open(file, "w") as f:
    for i in range(1,20):
        texto = f"{i} x {n} = {i*n}\n"
        f.write(texto)
with open(file) as f:
    texto = f.read()
print(texto)