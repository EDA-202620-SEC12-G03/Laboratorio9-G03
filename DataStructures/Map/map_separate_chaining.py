import random as rd
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf


def new_map(num_elements, load_factor, prime=109345121):
    """
    Crea una nueva tabla de hash implementada con Separate Chaining.
    La tabla utiliza un ArrayList donde cada casilla contiene una LinkedList (bucket)
    para manejar colisiones.
    """
    capacity = mf.next_prime(int(num_elements / load_factor))
    scale = rd.randint(1, prime - 1)
    shift = rd.randint(0, prime - 1)
    table = al.new_list()

    mapa = {
        "prime": int(prime),
        "capacity": int(capacity),
        "scale": int(scale),
        "shift": int(shift),
        "table": table,
        "current_factor": 0.0,
        "limit_factor": float(load_factor),
        "size": 0
    }

    # Inicializar cada balde (bucket) con una lista encadenada simple
    for _ in range(capacity):
        bucket = sll.new_list()
        al.add_last(mapa["table"], bucket)

    return mapa


def default_compare(key, entry):
    """
    Compara una llave con la llave almacenada en una entrada (entry).
    Retorna 0 si son iguales, 1 si key > entry_key, y -1 en caso contrario.
    """
    entry_key = me.get_key(entry)
    if key == entry_key:
        return 0
    elif key > entry_key:
        return 1
    return -1


def put(mapa, key, value):
    """
    Inserta o actualiza una pareja (key, value) en la tabla.
    Si la llave ya existe, actualiza su valor.
    Si sobrepasa el factor de carga límite, ejecuta el rehash.
    """
    hash_val = mf.hash_value(mapa, key)
    bucket = al.get_element(mapa["table"], hash_val)

    # Buscar si la llave ya se encuentra en el encadenamiento
    node = bucket["first"]
    found = False
    while node is not None:
        entry = node["info"]
        if me.get_key(entry) == key:
            me.set_value(entry, value)
            found = True
            break
        node = node["next"]

    if not found:
        entry = me.new_map_entry(key, value)
        sll.add_last(bucket, entry)
        mapa["size"] += 1
        mapa["current_factor"] = mapa["size"] / mapa["capacity"]

        if mapa["current_factor"] > mapa["limit_factor"]:
            mapa = rehash(mapa)

    return mapa


def contains(mapa, key):
    """
    Verifica si una llave existe en la tabla de hash.
    """
    hash_val = mf.hash_value(mapa, key)
    bucket = al.get_element(mapa["table"], hash_val)

    node = bucket["first"]
    while node is not None:
        entry = node["info"]
        if me.get_key(entry) == key:
            return True
        node = node["next"]
    return False


def get(mapa, key):
    """
    Retorna el valor asociado a la llave. Si la llave no existe, retorna None.
    """
    hash_val = mf.hash_value(mapa, key)
    bucket = al.get_element(mapa["table"], hash_val)

    node = bucket["first"]
    while node is not None:
        entry = node["info"]
        if me.get_key(entry) == key:
            return me.get_value(entry)
        node = node["next"]
    return None


def remove(mapa, key):
    """
    Elimina un elemento de la tabla por su llave si existe.
    Actualiza el tamaño y el factor de carga de la tabla.
    """
    hash_val = mf.hash_value(mapa, key)
    bucket = al.get_element(mapa["table"], hash_val)

    node = bucket["first"]
    pos = 0
    found = False
    while node is not None:
        entry = node["info"]
        if me.get_key(entry) == key:
            found = True
            break
        node = node["next"]
        pos += 1

    if found:
        sll.delete_element(bucket, pos)
        mapa["size"] -= 1
        mapa["current_factor"] = mapa["size"] / mapa["capacity"]

    return mapa


def size(mapa):
    """
    Retorna el número de elementos insertados en la tabla.
    """
    return mapa["size"]


def is_empty(mapa):
    """
    Retorna True si la tabla está vacía, False en caso contrario.
    """
    return mapa["size"] == 0


def key_set(mapa):
    """
    Retorna un ArrayList con todas las llaves almacenadas en el mapa.
    """
    keys = al.new_list()
    table = mapa["table"]

    for i in range(al.size(table)):
        bucket = al.get_element(table, i)
        node = bucket["first"]
        while node is not None:
            entry = node["info"]
            al.add_last(keys, me.get_key(entry))
            node = node["next"]

    return keys


def value_set(mapa):
    """
    Retorna un ArrayList con todos los valores almacenados en el mapa.
    """
    values = al.new_list()
    table = mapa["table"]

    for i in range(al.size(table)):
        bucket = al.get_element(table, i)
        node = bucket["first"]
        while node is not None:
            entry = node["info"]
            al.add_last(values, me.get_value(entry))
            node = node["next"]

    return values


def rehash(mapa):
    """
    Aumenta la capacidad de la tabla al siguiente número primo cercano al doble
    de la capacidad actual y reinserta todos los elementos existentes.
    """
    old_table = mapa["table"]
    new_m = new_map(mapa["capacity"] * 2, mapa["limit_factor"])

    for i in range(al.size(old_table)):
        bucket = al.get_element(old_table, i)
        node = bucket["first"]
        while node is not None:
            entry = node["info"]
            new_m = put(new_m, me.get_key(entry), me.get_value(entry))
            node = node["next"]

    mapa.update(new_m)
    return mapa