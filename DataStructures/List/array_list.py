def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def size(list):
    return list["size"]

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cpm_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cpm_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(list, element):
    list["elements"].insert(0, element)
    list["size"] += 1

def add_last(list, element):
    list["elements"].append(element)
    list["size"] += 1
    

def first_element(list):
    if not is_empty(list):
        return list["elements"][0]

def is_empty(list):
    if list["size"] <= 0:
        return True
    return False

def last_element(list):
    if not is_empty(list):
        return list["elements"][list["size"]]

def delete_element(list, pos):
    if pos < list["size"] and pos >= 0:
        list["elements"].pop(pos)
        list["size"] -= 1
    return list

def remove_first(list):
    if not is_empty(list):
        list["size"] -= 1
        return list["elements"].pop(0)
    raise IndexError("list index out of range")
    
def remove_last(list):
    if not is_empty(list):
        list["size"] -= 1
        return list["elements"].pop(list["size"] - 1)
    raise IndexError("list index out of range")

def insert_element(list, element, pos):
    if is_empty(list) and pos == 0:
        list["size"] += 1
        return list["elements"].insert(pos, element)
    elif pos < list["size"] and pos >= 0:
        list["size"] += 1
        return list["elements"].insert(pos, element)
    # raise IndexError("list index out of range")
    return list

def change_info(list, pos, info):
    if pos < list["size"] and pos >= 0:
        list["elements"][pos] = info
    return list

def exchange(list, pos1, pos2):
    if pos1 < list["size"] and pos1 >= 0 and pos2 < list["size"] and pos2 >= 0:
        list["elements"][pos1], list["elements"][pos2] = list["elements"][pos2], list["elements"][pos1]
    return list

def sub_list(lista, pos, num):
    if pos <= size(lista) and pos >= 0:
        new = new_list()
        for i in range(pos, num + pos):
            add_last(new, get_element(lista, i))
        return new
    raise IndexError("List index out of range")
    
def selection_sort(lst, sort_crit):
    tamano = size(lst)
    pos1 = 1
    while pos1 < tamano:
        minimum = pos1
        pos2 = pos1 + 1
        while (pos2 < tamano):
            if (sort_crit(get_element(lst, pos2), (get_element(lst, minimum)))):
                minimum = pos2 # minimum = posición elemento más pequeño
            pos2 += 1
        exchange(lst, pos1, minimum)
        pos1 += 1
    return lst


def insertion_sort(lst:list, sort_crit):
    tamano = size(lst)
    pos1 = 1
    while pos1 < tamano:
        pos2 = pos1
        while (pos2>1) and sort_crit(get_element(lst,pos2), get_element(lst, pos2-1)):
            exchange(lst,pos2,pos2-1)
            pos2 -=1
        pos1 += 1
    return lst

def default_sort_criteria(num1, num2):

    is_sorted = False
    if num1 < num2:
        is_sorted = True
    return is_sorted        
        
def shell_sort(lst, sort_crit):
    pass
    n = size(lst)
    h = 1
    while h < n//3: 
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and sort_crit(get_element(lst, j),
                get_element(lst, j-h)):
                exchange(lst, j, j-h)
                j -= h
        h //= 3 
    return lst

def merge_sort(lista, sort_crit):
    tamano = size(lista)
    if tamano > 1:
        mid = (tamano//2)

        leftlist = sub_list(lista, 0, mid)
        rightlist = sub_list(lista, mid, tamano - mid)

        merge_sort(leftlist, sort_crit)
        merge_sort(rightlist, sort_crit)

        i = j = k = 0

        leftelements = size(leftlist)
        rightelements = size(rightlist)

        while (i < leftelements) and (j < rightelements):
            elemei = get_element(leftlist, i)
            elemej = get_element(rightlist, j)

            if sort_crit(elemej, elemei):

                change_info(lista, k, elemej)
                j += 1
            else:
                change_info(lista, k, elemei)
                i += 1
            k += 1 # recore lista original a la mitad
            
        while i < leftelements: # i la recorre desde el comienso
            change_info(lista, k, get_element(leftlist, i))
            i += 1
            k += 1
        while j < rightelements:
            change_info(lista, k, get_element(rightlist, j))
            j += 1
            k += 1
    return lista

def quick_sort(lista, sort_crit):
    quick_sort2(lista, 1, size(lista), sort_crit)
    return lista

def quick_sort2(lista, lo, hi, sort_crit):

    if (lo >= hi):
        return
    pivot = partition(lista, lo, hi, sort_crit)
    quick_sort2(lista, lo, pivot-1, sort_crit)
    quick_sort2(lista, pivot+1, hi, sort_crit)

def partition(lista, lo, hi, sort_crit):

    follower = leader = lo
    while leader < hi:
        if (sort_crit(get_element(lista, leader),
        get_element(lista, leader))):

            exchange(lista, follower, leader)
            follower += 1
        leader += 1
    exchange(lista, follower, hi)
    return follower


"""abc = new_list()

add_last(abc, "R")
add_last(abc, "T")
add_last(abc, "I")
add_last(abc, "J")
add_last(abc, "K")
add_last(abc, "D")
add_last(abc, "A")
add_last(abc, "S")

print(merge_sort(abc, default_sort_criteria))"""