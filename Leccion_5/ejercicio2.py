def es_primo(num):
	for numero in range(2,num):
		if num%numero == 0:
			return "No es primo"
	else:
		return "Es Primo"


print(es_primo(16))
print(es_primo(7))

