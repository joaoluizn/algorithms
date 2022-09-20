"""
- Binary Search Implementation
- Time Complexity: BigO(LogN)
"""

def binary_search(list, target):
    baixo = 0
    alto = len(list) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        
        if list[meio] == target:
            return meio
        elif list[meio] < target:
            baixo = meio + 1
        else:
            alto = meio - 1
    return None
