# Buscar menor em um array

array = [85,96,57,82]

def buscaMenor(arr):
    menor = arr[0] 
    menor_indice = 0 
    for i in range(1, len(arr)):
        if arr[i] < menor: 
            menor = arr[i]
            menor_indice = i
    return menor_indice

print(buscaMenor(array))

# ordenar o um Array, usando a busca do menor pra criar um novo array
def ordenacaoPorSelecao(arr):
    novoArr = []
    while len(arr) > 0:
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr
    
print(ordenacaoPorSelecao(array))
