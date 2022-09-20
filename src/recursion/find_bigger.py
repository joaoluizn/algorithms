""" Divide to conquer - Count elements in list with recursion """

def find_bigger(list):
    bigger = 0
    
    if len(list) == 1:
        bigger = list[0]
    elif len(list) > 1:
        bigger = max(list.pop(), find_bigger(list))
        
    return bigger
