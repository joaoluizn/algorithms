""" Divide to Conquer Sum list using Recursion """

def sum_list(list):
    sum = 0

    if len(list) > 1:
        sum = list.pop() + sum_list(list)
    elif len(list) == 1:
        sum += list[0]
    return sum
