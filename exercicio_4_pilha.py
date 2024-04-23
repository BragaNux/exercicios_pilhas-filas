def esta_vazia(self):
        return len(self.itens) == 0

def esvazia(p):
    while not p.esta_vazia():  # Enquanto a pilha não estiver vazia
        p.pop()  # Remove o elemento do topo da pilha
