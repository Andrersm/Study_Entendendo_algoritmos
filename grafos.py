# implementação basica de um Grafo


# grafo = {}
# grafo["voce"] = ["alice", "bob", "claire"]


# Um Grafo maior 

grafo = {}
grafo["voce"] = ["bob", "claire", "alice"] 
grafo["bob"] = ["anuj", "peggy"] 
grafo["alice"] = ["peggy"] 
grafo["claire"] = ["thom", "jonny"] 
grafo["anuj"] = [] 
grafo["peggy"] = [] 
grafo["thom"] = [] 
grafo["jonny"] = []

# print(grafo)

# Pergunta rápida: A ordem que adiciona os pares chave/valor faz diferença?
# Existe diferença ao escrever 
# grafo["claire"] = ["thom", "jonny"] 
# grafo["anuj"] = [] 
# em vez de 
# grafo["anuj"] = [] 
# grafo["claire"] = ["thom", "jonny"]

# Resposta: Não faz diferença, pois as tabelas hash não são ordenadas. 
# Portanto não importa em que ordem você adiciona os pares chave/valor

# exemplo de uso de uma pesquisa em largura. aqui estou procurando baseado na
# ultima letra do nome da pessoa. voce pode ir testando outras letras.
# pra entender como a busca funciona. mudando a ordem. da fila. pois a fila
# segue a ordem que foi implementada. logo se eu coloquei o "y" como ultima 
# letra pra decidir quem é o vendedor o "peggy" vai aparecer antes. pois ele foi.
# colocado na fila antes do jonny por exemplo. mas fique livre pra testar.
# não esquecer de adicionar uma fila de verificados. se não podemos entrar em
# um LOOP infinito. pois um ADD o outro a fila.
from collections import deque

def pessoa_e_vendedor(nome): 
    return nome[-1] == 'y'

def busca_vendedor(grafo, nome_inicial):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome_inicial]
    verificadas = [] 


    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):  
                print(pessoa + " é um vendedor de manga!") 
                return True
            else: 
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa) 

    
    return False

print(busca_vendedor(grafo, "voce"))




