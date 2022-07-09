
# GENERO LISTA UTILIZO SPLIT PARA SEPARAR POR COMA(,) y luego hago un set para eliminar los elementos duplicados
lista = set(input("Ingrese lista de paises separados por coma:").split(","))

#Imprimo en consola los elementos del set de manera ordenada alfabeticamente

print(",".join(list(sorted(lista))))


