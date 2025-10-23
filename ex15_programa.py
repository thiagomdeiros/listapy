lista_de_compras = []

print("Menu da Lista de Compras")
print("1 Adicionar item")
print("2 Remover item")
print("3 Mostrar lista")
print("4 Sair")

while True:
    escolha = input("Escolha uma opção (1-4): ")
    if escolha == "1":
        item = input("Digite o item para adicionar: ")

        lista_de_compras.append(item)
        print(f"'{item}' adicionado à lista.")

    elif escolha == "2":

        item = input("Digite o item para remover: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"'{item}' removido da lista.")
        else:
            print(f"O item '{item}' não está na lista.")
    elif escolha == "3":
        print("Lista de Compras")
        print(lista_de_compras)
    elif escolha == "4":
        print("Saindo do programa")
        break
