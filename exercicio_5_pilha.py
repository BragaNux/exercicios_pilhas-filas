class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            return None

def palindromo(palavra):
    pilha = Pilha()

    # Adiciona cada letra da palavra na pilha
    for letra in palavra:
        pilha.push(letra)

    # Reconstrói a palavra invertida
    palavra_invertida = ""
    while not pilha.esta_vazia():
        palavra_invertida += pilha.pop()

    # Verifica se a palavra original é igual à palavra invertida
    return palavra == palavra_invertida

palavra = "arara"
print(palindromo(palavra))  # Saída: True

palavra = "radar"
print(palindromo(palavra))  # Saída: True

palavra = "python"
print(palindromo(palavra))  # Saída: False
