# 2. Implemente uma função que receba 3 filas, f_res, f1 e f2, e transfira
# alternadamente os elementos de f1 e f2 para f_res, conforme ilustrado a
# seguir:

# Note que, ao final desta função, as filas f1 e f2 vão estar vazias, e a fila f_res
# vai conter todos os elementos originalmente em f1 e f2 (inicialmente f_res
# está vazia). Esta função deve obedecer ao protótipo:


def combina_filas(f_res, f1, f2):
    while not f1.esta_vazia() and not f2.esta_vazia():
        f_res.enfileirar(f1.desenfileirar())  # Transferir elemento de f1 para f_res
        f_res.enfileirar(f2.desenfileirar())  # Transferir elemento de f2 para f_res
    
    # Verificar se ainda há elementos em f1 e transferi-los para f_res
    while not f1.esta_vazia():
        f_res.enfileirar(f1.desenfileirar())
    
    # Verificar se ainda há elementos em f2 e transferi-los para f_res
    while not f2.esta_vazia():
        f_res.enfileirar(f2.desenfileirar())
