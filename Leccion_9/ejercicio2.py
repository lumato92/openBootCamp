import functools

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,30]



#funcion que evalua un numero y retorna el mismo si es impar
def impar(num):
    if num%2 != 0:
        return num
    
#Uso filter para recorrer la lista y evaluar cada item de la misma con la funcion impar
resultado = list(filter(impar, lista1))


print(resultado)

#Con reduce le paso una funcion lambda que suma los valores de la lista

print(functools.reduce(lambda a,b : a+b , resultado))