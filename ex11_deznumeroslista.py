print("Digite 10 números inteiros: ")

numeros = [
    int(input("n1: ")),
    int(input("n2: ")),
    int(input("n3: ")),
    int(input("n4: ")),
    int(input("n5: ")),
    int(input("n6: ")),
    int(input("n7: ")),
    int(input("n8: ")),
    int(input("n9: ")),
    int(input("n10: "))
]

maiores_que_10 = sum([
    numeros[0] > 10,
    numeros[1] > 10,
    numeros[2] > 10,
    numeros[3] > 10,
    numeros[4] > 10,
    numeros[5] > 10,
    numeros[6] > 10,
    numeros[7] > 10,
    numeros[8] > 10,
    numeros[9] > 10
])

print("Numeros maiores que 10:", maiores_que_10)
