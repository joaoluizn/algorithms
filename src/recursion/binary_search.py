""" Binary Search Using Recursion - Divide to Conquer """


def binary_search(list, target):
    valor = None
    inicio = 0
    fim = len(list) - 1
    
    if inicio <= fim:
        meio = (inicio + fim) // 2
    
        if list[meio] == target:
            valor = list[meio]

        elif list[meio] < target:
            valor = binary_search(list[meio + 1:], target)

        else:
            valor = binary_search(list[:meio - 1], target)

    return valor
