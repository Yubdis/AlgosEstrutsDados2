"""
exercisios para aula 2 fazer um algoritmo de Busca sequencial e um algoritmo de busca binaria

Você deverá implementar um algoritmo que execute a mesma função do método index() já
implementado na estrutura de dados lista do python.
minha_lista.index(elemento)

Crie uma função que receba como parâmetros uma lista e a informação a ser encontrada
nesta lista.
Esta função deverá retornar a posição da lista onde a informação foi encontrada,
ou retornar None, caso a informação não seja encontrada.

"""

def busca_sequencial(lista, elemento):
    indice = 0

    for i in lista:
        if i == elemento:
            return indice
        indice += 1
    return None

print (busca_sequencial([1, 2, 3, 4, 5], 3))  # Deve retornar 2

def busca_binaria(lista, elemento):
    num_left = 0
    num_end = len(lista) - 1

    while num_left <= num_end:
        meio = (num_left + num_end) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            num_left = meio + 1
        else:
            num_end = meio - 1
    return None

print(busca_binaria([1, 2, 3, 4, 5], 3))  # Deve retornar 2