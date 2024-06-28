

# Pesquisa binária
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    print(f"baixo: {baixo}, alto: {alto}")


    while baixo <= alto:
        meio = (baixo + alto) // 2
        print(f"meio: {meio}")
        chute = lista[meio]
        print(f"chute: {chute}")
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
            print(f"if chute maior que o item alto: {alto}")
        else:
            baixo = meio + 1
            print(f" else baixo: {baixo}")
    return None

minha_lista = list(range(1, 101))

print(pesquisa_binaria(minha_lista, 20))