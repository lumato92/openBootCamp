

# CREO EL ARCHIVO Y LUEGO LO CIERRO
file = open("archivo.txt","w")

file.close()

# ABRO EL ARCHIVO y escribo un contenido

with open("./Leccion_8/archivo.txt","w") as f:
    f.write("Hola este es un archivo generado con python \n")

# ABRO NUEVAMENTE EL ARCHIVO Y LEO

with open("./Leccion_8/archivo.txt","r") as file:

    print(file.read())


#Abro el archivo nuevamente y le escribo otra linea luego cierro , vuelvo a abrirlo y muestro el contenido

with open("./Leccion_8/archivo.txt","a") as f:
    f.write("Hola esta es la linea 2 \n")

with open("./Leccion_8/archivo.txt","r") as f:
    print(f.read())
