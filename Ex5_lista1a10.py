numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [2, 4, 6, 8, 10]
impares = [1, 3, 5, 7, 9]

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("Números pares:", pares)
print("Números ímpares:", impares)
