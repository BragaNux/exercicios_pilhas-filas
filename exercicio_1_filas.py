##1. Faça um programa que imprima uma fila, representada como vetor (filacircular) e como lista.



class FilaCircular:
    def __init__(self, capacidade_maxima):
        self.capacidade_maxima = capacidade_maxima  # Define a quantidade máxima de elementos que a fila pode armazenar
        self.fila = [None] * self.capacidade_maxima  # Inicializa uma lista vazia com a capacidade máxima definida
        self.primeiro_elemento = self.ultimo_elemento = -1  # Define os marcadores de posição da fila como -1, indicando que a fila está vazia

    def enfileirar(self, item):
        if (self.ultimo_elemento + 1) % self.capacidade_maxima == self.primeiro_elemento:  # Verifica se a fila está cheia
            print("A fila está cheia - não é possível enfileirar mais elementos")
        elif self.primeiro_elemento == -1:  # Verifica se a fila está vazia
            self.primeiro_elemento = self.ultimo_elemento = 0  # Se estiver vazia, define o marcador de primeiro elemento como 0
            self.fila[self.ultimo_elemento] = item  # Enfileira o item na posição do último elemento
        else:
            self.ultimo_elemento = (self.ultimo_elemento + 1) % self.capacidade_maxima  # Atualiza o marcador de último elemento
            self.fila[self.ultimo_elemento] = item  # Enfileira o item na posição do último elemento

    def desenfileirar(self):
        if self.primeiro_elemento == -1:  # Verifica se a fila está vazia
            print("A fila está vazia - não é possível desenfileirar")
        elif self.primeiro_elemento == self.ultimo_elemento:  # Verifica se há apenas um elemento na fila
            item = self.fila[self.primeiro_elemento]  # Armazena o item a ser desenfileirado
            self.primeiro_elemento = self.ultimo_elemento = -1  # Define os marcadores de posição como -1, indicando que a fila está vazia
            return item
        else:
            item = self.fila[self.primeiro_elemento]  # Armazena o item a ser desenfileirado
            self.primeiro_elemento = (self.primeiro_elemento + 1) % self.capacidade_maxima  # Atualiza o marcador de primeiro elemento
            return item

    def exibir(self):
        if self.primeiro_elemento == -1:  # Verifica se a fila está vazia
            print("A fila está vazia")
        else:
            print("Elementos da fila:")
            i = self.primeiro_elemento
            while True:
                print(self.fila[i], end=" ")  # Exibe o elemento na posição atual
                if i == self.ultimo_elemento:  # Verifica se chegou ao último elemento da fila
                    break
                i = (i + 1) % self.capacidade_maxima  # Atualiza a posição para o próximo elemento
            print()


def main():
    capacidade_maxima = 5  # Define a capacidade máxima da fila
    fila = FilaCircular(capacidade_maxima)  # Cria uma nova fila circular com a capacidade máxima definida

    # Enfileirando elementos
    for i in range(1, capacidade_maxima + 2):  # Enfileira elementos de 1 a capacidade_maxima + 1
        fila.enfileirar(i)  # Enfileira o elemento na fila

    # Exibindo a fila
    fila.exibir()


if __name__ == "__main__":
    main()
