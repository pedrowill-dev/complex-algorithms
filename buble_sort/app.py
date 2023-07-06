def buble_sort(items):

    for _ in range(1, len(items) + 1):
        for item_atual in range(len(items) -1, -1, -1):
            if items[item_atual] < items[item_atual - 1]:
                ultimo_valor, anterior_valor = items[item_atual], items[item_atual - 1]
                if item_atual - 1 < 0:
                    break
                items[item_atual] = anterior_valor
                items[item_atual - 1]  = ultimo_valor

    return items


lista_n_ordenada = [10,2,5,4,3,1,0,8,9]

lista_ordenada = buble_sort(lista_n_ordenada)
print(lista_ordenada)