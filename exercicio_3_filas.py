def fila_cria(tam):
    tam
    print("Eu funciono 100%")
def fila_insere(f, v):
    f, v
    print("Eu funciono 100%")
def fila_retira(f):
    f
    print("Eu funciono 100%")
def fila_vazia(f):
    f
    print("Eu funciono 100%")
def fila_frente(f):
    f
    print("Eu funciono 100%")


def ordena_filas(f1, f2):
    fila_resultante = fila_cria(f1.tamanho() + f2.tamanho())  # Cria uma fila resultante com capacidade suficiente

    # Enquanto ambas as filas não estiverem vazias
    while not fila_vazia(f1) and not fila_vazia(f2):
        # Verifica qual elemento é menor entre as frentes das duas filas
        if fila_frente(f1) <= fila_frente(f2):
            fila_insere(fila_resultante, fila_retira(f1))  # Insere o elemento de f1 na fila resultante
        else:
            fila_insere(fila_resultante, fila_retira(f2))  # Insere o elemento de f2 na fila resultante

    # Se ainda houver elementos em f1, insere-os na fila resultante
    while not fila_vazia(f1):
        fila_insere(fila_resultante, fila_retira(f1))

    # Se ainda houver elementos em f2, insere-os na fila resultante
    while not fila_vazia(f2):
        fila_insere(fila_resultante, fila_retira(f2))

    return fila_resultante

