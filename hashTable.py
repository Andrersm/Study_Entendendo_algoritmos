# python á tem implementado né 

# posso aqui criar com a fuunção

caderno = dict()

# ou 

cadernos = {'maça': 1,
            'laranja': 20}

print(cadernos)


lista_telefonica = {}

lista_telefonica["jenny"] = 8675309

lista_telefonica["emergency"] = 911

print(lista_telefonica["jenny"])


voted = {} 

def verifica_eleitor(nome): 
    if voted.get(nome): 
        print("Mande embora!")
    else: 
        voted[nome] = True
        print("Deixe votar!")

print(verifica_eleitor("tom"))
print(verifica_eleitor("mike"))
print(verifica_eleitor("mike"))

# a baixo mais ou menos como seria o funcionamente de um cache em uma aplicação
# se tiver os dados. tu ja entrega pro usuario. caso contrario. tu requisita pro
# servidor
# cache = {}
# def pega_pagina(url):
#     if cache.get(url):
#         return cache[url]
#     else: 
#         dados = pega_dados_do_servidor(url)
#         cache[url] = dados ❷ return dados





