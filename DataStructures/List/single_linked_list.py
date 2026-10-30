def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist


def size(my_list):
    return my_list["size"]


def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]


def is_present(my_list, element, cpm_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:  # temp != None ???
        if cpm_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count


def add_first(my_list, element):
    if is_empty(my_list):
        nuevo = {"info": element, "next": None}
        my_list["first"] = nuevo
        my_list["last"] = nuevo
    else:
        nuevo = {"info": element, "next": my_list["first"]}
        my_list["first"] = nuevo
    my_list["size"] += 1


def add_last(lista, element):
    nuevo = {"info": element, "next": None}
    if is_empty(lista):
        lista["first"] = nuevo
        lista["last"] = nuevo
    else:
        lista["last"]["next"] = nuevo
        lista["last"] = nuevo
    lista["size"] += 1


def first_element(lista):
    if lista["size"] > 0:
        return lista["first"]["info"]


def is_empty(lista):
    if lista["size"] <= 0:
        return True
    return False


def last_element(lista):
    if lista["size"] > 0:
        return lista["last"]


def delete_element(lista, pos: int):
    if pos >= 0 and pos < lista["size"]:
        if pos == 0:
            lista["first"] = lista["first"]["next"]
        elif pos > 0:
            current_node = lista["first"]
            previous_node = lista["first"]
            i = 1
            while i < pos:
                previous_node = current_node
                current_node = current_node["next"]
                previous_node["next"] = current_node["next"]
                if current_node == lista["last"]:
                    lista["last"] = previous_node
                i += 1
        lista["size"] -= 1
        return lista
    raise IndexError("list index out of range")


def remove_first(lista):
    if lista["size"] > 0:
        deleted_element = lista["first"]["info"]
        lista["first"] = lista["first"]["next"]
        lista["size"] -= 1
        if lista["size"] == 0:
            lista["last"] = None
        return deleted_element
    raise IndexError("list index out of range")


def remove_last(lista):
    if lista["size"] > 0:
        deleted_element = lista["last"]["info"]
        if lista["first"] == lista["last"]:
            lista["first"] = None
            lista["last"] = None
        else:
            current_node = lista["first"]
            while current_node["next"] != lista["last"]:
                current_node = current_node["next"]
            lista["last"] = current_node
            lista["last"]["next"] = None
        lista["size"] -= 1
        return deleted_element
    raise Exception("list index out of range")


def insert_element(lista, element, pos: int):
    if 0 <= pos < lista["size"]:
        if pos == 0:
            add_first(lista, element)
        elif pos == lista["size"] - 1:
            add_last(lista, element)
        elif 0 < pos < lista["size"] - 1:
            nuevo = {"info": element, "next": None}
            current_node = lista["first"]["next"]
            previous_node = lista["first"]
            i = 1
            while i < pos:
                previous_node = current_node
                current_node = current_node["next"]
                previous_node["next"] = current_node["next"]
            nuevo["next"] = current_node
            previous_node["next"] = nuevo
        lista["size"] += 1
        return lista
    raise Exception("list index out of range")


def change_info(lista, pos: int, new_info):
    if 0 <= pos < lista["size"]:
        if pos == 0:
            lista["first"]["info"] = new_info
        elif pos > 0:
            current_node = lista["first"]["next"]
            i = 1
            while i < pos:
                current_node = current_node["next"]
                i += 1
            current_node["info"] = new_info
        return lista
    raise Exception("list index out of range")


def exchange(lista, pos1, pos2):
    if (0 <= pos1 < lista["size"] and 0 <= pos2 < lista["size"]):
        info1 = get_element(lista, pos1)
        info2 = get_element(lista, pos2)

        change_info(lista, pos1, info2)
        change_info(lista, pos2, info1)
        return lista
    IndexError("Index out of range")

def sub_list(lista, pos: int, num_elements: int):
    if pos < 0 or pos > lista["size"] or num_elements < 0:
        raise Exception("list index out of range")

    nueva = new_list()
    limite = min(pos + num_elements, lista["size"])
    i = pos
    while i < limite:
        add_last(nueva, get_element(lista, i))
        i += 1
    return nueva


def default_sort_criteria(num1, num2):
    is_sorted = False
    if num1 < num2:
        is_sorted = True
    return is_sorted


def selection_sort(lst, sort_crit):
    tamano = size(lst)
    pos1 = 0
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
    pos1 = 0
    while pos1 < tamano:
        pos2 = pos1
        while (pos2>1) and sort_crit(get_element(lst,pos2), get_element(lst, pos2-1)):
            exchange(lst,pos2,pos2-1)
            pos2 -=1
        pos1 += 1
    return lst


def shell_sort(lst, sort_crit):
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


