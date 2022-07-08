

# CREO EL ARCHIVO Y LUEGO LO CIERRO
file = open("archivo.txt","w")

file.close()

# ABRO EL ARCHIVO y escribo un contenido

with open("./Leccion_8/archivo.txt","w") as f:
    f.write("Hola este es un archivo generado con python \n")

