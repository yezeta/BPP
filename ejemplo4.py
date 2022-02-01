import pdb

"""
Haciendo uso de comprensión de listas realice un programa que, dado 
una lista de listas de números enteros, devuelva el máximo de cada 
lista.
"""
def maxlista(n):
    pdb.set_trace()
    lista = list(n)
    maxlistas = [max(i) for i in lista]
    return maxlistas

listanum = [[2,4,1],[1,2,3,4,5,6,7,8],[100,250,4]]
print(maxlista(listanum))

"""
Haga uso de la función filter para construir un programa que, dado 
una lista de n números devuelva aquellos que son primos. 
"""
def es_primo(n):
    primo = True
    for i in range(2,n):
        if(n%i == 0):
            primo = False
    return primo

lista1 = [3, 4, 8, 5, 5, 22, 13]
primos = list(filter(es_primo,lista1))
print(primos)