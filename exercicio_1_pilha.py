def imprimir_pilha(pilha):
    if len(pilha) == 0:  # Verifica se a pilha está vazia
        print("A pilha está vazia")
    else:
        print("Valores armazenados na pilha:")
        for valor in reversed(pilha):  # Itera sobre os valores da pilha de trás para frente
            print(valor)
