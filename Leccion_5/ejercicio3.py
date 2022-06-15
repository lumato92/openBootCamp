def leap_year(year):

	if (year%4== 0) and (year%100 != 0) or (year % 400 ==0):
		print(f"El año {year} es Bisiesto")

	else:
		print(f"El año {year} no es Bisiesto")	

leap_year(int(input("Ingrese el año: ")))
