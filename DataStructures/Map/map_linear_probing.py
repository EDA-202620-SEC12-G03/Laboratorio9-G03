import random as rd
from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def new_map(num_elements, load_factor, prime = 109345121):
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
        "current_factor": 0,
        "limit_factor": float(load_factor), # Limite antes de hacer rehash
        "size" : int(0),
        "collisions": int(0)
    }
    i=0
    while i < capacity:
        entry = me.new_map_entry(None, None)
        al.add_last(mapa["table"], entry)
        i += 1
    return mapa
    
def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True # Encontro un espacio
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0: # Que el valor corresponda a la llave
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
      if found != True:
        my_map["collisions"] += 1
   return ocupied, first_avail

def is_available(table, pos):

   entry = al.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1 
   return -1

def rehash(mapa):
    old = mapa["table"]
    new = new_map(mapa["capacity"] * 2, mapa["limit_factor"])

    for pos in range(al.size(old)):
        entry = al.get_element(old, pos)
        key = me.get_key(entry)

        if key is not None and key != "__EMPTY__":
            new = put(new, key, me.get_value(entry))

    return new

def put(mapa: dict, key, value)-> dict:
    _hash = mf.hash_value(mapa, key)
    found, index = find_slot(mapa, key, _hash)
    
    if found:
        current = al.get_element(mapa["table"], index)
        me.set_value(current, value)
    else:
        mapa["size"] += 1
        entry = me.new_map_entry(key, value)
        mapa["current_factor"] = mapa["size"]/mapa["capacity"]
        al.change_info(mapa["table"], index, entry)
        if mapa["current_factor"] > mapa["limit_factor"]:
            mapa = rehash(mapa)
    return mapa
         
    
def contains(mapa, key):
    """
    Verifica que una llave existe dentro de la tabla
    """
    _hash = mf.hash_value(mapa, key)
    ocupied, index = find_slot(mapa, key, _hash)
    return ocupied
    
def get(mapa, key):
    
    _hash = mf.hash_value(mapa, key)
    found, index = find_slot(mapa, key, _hash)

    if found:
        entry = al.get_element(mapa["table"], index)
        return me.get_value(entry)
    return None
    
    
def remove(mapa, key):
    """
    Elimina una llave del mapa.

    Si la llave existe:
    - Cambia la llave y el valor por "__EMPTY__".
    - Reduce el tamaño del mapa.
    - Actualiza el factor de carga.
    - Retorna el valor eliminado.

    Si la llave no existe, retorna None.
    """
    hash_value = mf.hash_value(mapa, key)
    found, index = find_slot(mapa, key, hash_value)

    if not found:
        return None

    entry = al.get_element(mapa["table"], index)
    # removed_value = me.get_value(entry)

    me.set_key(entry, "__EMPTY__")
    me.set_value(entry, "__EMPTY__")

    mapa["size"] -= 1
    mapa["current_factor"] = mapa["size"] / mapa["capacity"]

    return mapa
    
    
def size(mapa):
    return mapa["size"]

def key_set(mapa):
    # Devuelve la lista de todas las llaves en la tabla
    lista = al.new_list()
    tabla = mapa["table"]
    for i in range(al.size(tabla)):
        current = al.get_element(tabla, i)
        if not is_available(tabla, i):
            al.add_last(lista, me.get_key(current))
    return lista

def value_set(mapa):
    """
    Devuelve una lista con todos los valores válidos del mapa.
    """
    lista = al.new_list()
    tabla = mapa["table"]

    for i in range(al.size(tabla)):
        current = al.get_element(tabla, i)

        if not is_available(tabla, i):
            al.add_last(lista, me.get_value(current))

    return lista

def is_empty(mapa):
    if mapa["size"] == 0:
        return True
    return False
