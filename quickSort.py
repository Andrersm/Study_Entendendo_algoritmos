# Exercicios anteiores de recursividade para entender o quickSort

# exercicio  4.1 Escreva o código para a função soma, vista anteriormente
# def soma(lista):
#     # Caso base: lista vazia
#     if not lista:
#         return 0
#     # Chamada recursiva: soma o primeiro elemento com o resultado da soma do resto da lista
#     else:
#         return lista[0] + soma(lista[1:])

# array = [2, 4, 6]
# resultado = soma(array)
# print(resultado) 

# exercicio 4.2 Escreva uma função recursiva que conte o número de itens em uma lista.
# a logica é muito parecida da primeira a diferença é e que aqui vou apenas somar toda vez que 
# for "entrando da call stack. no caso estou contando na verdade quando estiver "saindo"

# def conta_itens(lista):
#     # Caso base: lista vazia
#     if not lista:
#         return 0
#     # caso recursivo: conta o primeiro elemento e o resto da lista
#     else:
#         return 1 + conta_itens(lista[1:])

# array = [2, 4, 6]
# resultado = conta_itens(array)
# print(resultado)

# exercicio 4.3 Encontre o valor mais alto em uma lista.

array = [85,96,57,82]
def buscaMaior(arr):
    maior = arr[0] 
    maior_indice = 0 
    for i in range(1, len(arr)):
        if arr[i] > maior: 
            maior = arr[i]
            maior_indice = i
    return maior_indice

print(array[buscaMaior(array)])


# exercicio 4.4 Você se lembra da pesquisa binária do Capítulo 1? Ela também é um algoritmo
#  do tipo dividir para conquistar. Você consegue determinar o 
# caso-base e o caso recursivo para a pesquisa binária? Seria o Chute, se ele estiver certo
# eu acabo o algoritmo


# O algoritmo do quickSort em si 

def quicksort(array):
    if len(array) < 2:
         return array
    else: pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo] 
    maiores = [i for i in array[1:] if i > pivo] 
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 2, 3]))


# exercicios  Quanto tempo levaria, em notação Big O, para completar cada uma destas operações?

# 4.5 Imprimir o valor de cada elemento em um array
# Resposta: O(n) pois vai percorrer cada elemento.

# 4.6 Duplicar o valor de cada elemento em um array
# Resposta: O(n) novamente, pois vai passar por cada elemento e duplicar.

# 4.7 Duplicar o valor apenas do primeiro elemento do array
# Resposta: O(1) pois vai duplicar apenas o primeiro em qualquer ocasião, e se for um array, sempre sabemos que o primeiro elemento está no índice 0.

# 4.8 Criar uma tabela de multiplicação com todos os elementos do array
# Resposta: O(n²), simplesmente por ter que percorrer os elementos mais de uma vez, sendo um algoritmo bem lento no geral.









