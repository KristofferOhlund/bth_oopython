"module for sorting"

from src.unorderedlist import UnorderedList

def insertion_sort(lst:UnorderedList):
    """ Sorting unorderedlist with insertions sort """
    for i in range(1, lst.size()):
        current_value = lst.get(i)
        j = i
        while j > 0 and current_value < lst.get(j - 1):
            lst.set(j, lst.get(j - 1))  # Flyttar lättare element framåt
            j -= 1
        lst.set(j, current_value)

# denna funkar, bytte ut [ ] mot paranteser och
# satte j att vara > 0 istället för >=
# Fattar dock inte hur det funkar, ren chansning
# Vi måste sortera på tuples (första värdet)
def recursive_insertion(lst: UnorderedList, n):
    """ Sort lst recursivly, returns -1 if list i empty"""
    if lst:
        if n == 0:
            return lst
        recursive_insertion(lst, n - 1)
        j = n - 1
        current_value = lst.get(n - 1)
        while j > 0 and current_value < lst.get(j - 1):
            lst.set(j, lst.get(j - 1))
            j -= 1
        lst.set(j, current_value)
    else:
        return -1
    return lst
