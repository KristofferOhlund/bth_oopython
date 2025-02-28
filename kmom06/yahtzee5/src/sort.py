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

def recursive_insertion(lst, n):
    if n <= 1:
        return

    # Recursivt sortera för de första n-1 elementen
    recursive_insertion(lst, n - 1)

    current_value = lst[n - 1]
    current_points = current_value["points"]  # "points" för sortering. Vet inte om detta är ok eller inte?
    
    j = n - 2
    # Flytta större element framåt
    while j >= 0:
        prev_value = lst[j]
        prev_points = prev_value["points"]  # Jämför med "points"

        if prev_points < current_points:  # Om den föregående punkten är mindre, flytta
            lst[j + 1] = prev_value
        else:
            break  # Stoppa om vi har hittat rätt plats

        j -= 1

    # Placera de nuvarande värdet på rätt plats
    lst[j + 1] = current_value


#  "utan anpassning till points"
# def recursive_insertion(lst, n):
#     if n <= 1:
#         return lst

#     recursive_insertion(lst, n - 1)  

#     current_value = lst[n - 1]  
#     j = n - 2 

#     while j >= 0 and lst[j] > current_value:
#         lst[j + 1] = lst[j]  
#         j -= 1


#     lst[j + 1] = current_value

#     return lst


#detta funkar, men får det inte att funka med topplistan..
leaderboard = [
    {"name": "Rubi", "points": 28},
    {"name": "asdasd", "points": 51},
    {"name": "Kingen", "points": 58},
    {"name": "Test1", "points": 90},
    {"name": "test4", "points": 18}
]

# Sortera listan
size = len(leaderboard)  # storleken på listan dvs "n" i detta fall.
recursive_insertion(leaderboard, size)

# Utskrift efter sortering
print(f"Sorted Leaderboard:{leaderboard}")
