""" Divide to conquer - Count elements in list with recursion """

def count_elements(list):
    count = 0
    
    if len(list) >= 1:
        list.pop()
        count = 1 + count_elements(list)

    return count
 