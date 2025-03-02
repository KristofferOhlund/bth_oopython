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
    return -1

#detta funkar, men får det inte att funka med topplistan..
leaderboard = [
    {"name": "Rubi", "points": 28},
    {"name": "asdasd", "points": 51},
    {"name": "Kingen", "points": 58},
    {"name": "Test1", "points": 90},
    {"name": "test4", "points": 18}
]

# Sortera listan
# size = len(leaderboard)  # storleken på listan dvs "n" i detta fall.
# print(recursive_insertion(leaderboard, size))

# # Utskrift efter sortering
# print(f"Sorted Leaderboard:{leaderboard}")
