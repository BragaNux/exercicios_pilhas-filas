class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.pilha = [None] * capacidade

    def topo(self):
        if self.esta_vazia():
            raise Exception("A pilha está vazia")
        return self.pilha[self.topo]
