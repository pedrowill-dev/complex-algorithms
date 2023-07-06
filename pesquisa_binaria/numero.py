import time

# Função de pesquisa binária
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
    
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    
    return None

# Função de pesquisa simples
def pesquisa_simples(lista, item):
    for indice, valor in enumerate(lista):
        if valor == item:
            return indice
    
    return None

lista = [item for item in range(0, 5000000)]
item = 200000
inicio = time.time()
# Marca o tempo de fim
print(pesquisa_binaria(lista, item))
fim = time.time()
tempo_execucao = (fim - inicio) * 10000
print(tempo_execucao)