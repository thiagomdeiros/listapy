nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))
nota5 = float(input("Nota 5: "))

notas = [nota1, nota2, nota3, nota4, nota5]

soma = sum(notas)
quantidade = len(notas)
media = soma / quantidade

acima_da_media = sum([
    nota1 > media,
    nota2 > media,
    nota3 > media,
    nota4 > media,
    nota5 > media
])

print("Notas:", notas)
print(f"Média das notas: {media:.2f}")
print("Notas acima da média:", acima_da_media)
