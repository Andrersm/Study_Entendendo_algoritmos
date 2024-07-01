# Rercusão que vai entrar em looping infinito


#i = 10
#def regressiva(i):
#   print(i)
#    regressiva(i-1)
#
#print(regressiva(i))


# def regressiva(i):
#     print(i)
#     if i <= 0:
#         return 
#     else:
#         regressiva(i-1)

# print(regressiva(i))

def fat(x: int):
    if x == 1:
        return 1
    else :
        return x * fat(x - 1)
    
print(fat(999))

# em python o maximo de recursão sao 999 após isso "estoura" a recursão 
