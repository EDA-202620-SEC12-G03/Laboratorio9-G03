from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import array_list as al


# priority seria determinado por la direccion de la ruta y hora de partida
def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def priority(my_heap, parent:any, child:any):
    # Tu usas esta función directamente, no el default compare!
    try:
        return my_heap["cmp_function"](parent, child)
    except Exception as exp:
        raise RuntimeError("Error en priority")

def new_heap(is_min_pq=True):
    cmp_function = default_compare_higher_value
    if is_min_pq:
        cmp_function = default_compare_lower_value
    heap = {
            'elements': None,
            'size': 0,
            'cmp_function': cmp_function
            }
    
    heap['elements'] = al.new_list()
    # al.add_last(heap["elements"], None)
    
    return heap
    
def swim(heap: dict, idx: int) -> None:
    """_swim hace "swim", "sube" o "flota" "bottom-up reheapfy" el elemento en la posición idx del montículo (heap).

    Args:
        heap (dict): diccionario que representa el montículo (heap).
        idx (int): índice del elemento a hacer "swim".
    """
    try:     
        while idx > 0:
                _parent = al.get_element(heap["elements"], idx // 2)
                _element = al.get_element(heap["elements"], idx)
                if priority(heap, _parent, _element):
                    # Los cambia si el padre tiene mas prioridad - Se tiene que revisar si esto no va al revez
                    exchange(heap, idx, idx // 2) # Usamos exchange y no insert
                idx = idx // 2
    except Exception as exp:
        raise RuntimeError("Error en swim") from exp
        
def sink(hp: dict, idx: int) -> None:
    """_sink hace "sink", "baja" o "hundir" "top-down reheapfy" el elemento en la posición idx del montículo (heap).

    Args:
        hp (dict): diccionario que representa el montículo (heap).
        idx (int): índice del elemento a hacer "sink".
    """
    try:
        _size = hp["size"]
        while 2 * idx < _size:
            j = 2 * idx
            if j < _size:
                _elm1 = al.get_element(hp["elements"], j)
                _elm2 = al.get_element(hp["elements"], j + 1)
                if priority(hp, _elm1, _elm2):
                    # Tambien verificar aqui
                    j += 1
            _elm1 = al.get_element(hp["elements"], idx)
            _elm2 = al.get_element(hp["elements"], j)
            if not priority(hp, _elm1, _elm2):
                # Se tiene que verificar si proority no esta danto el resultado al revez
                break
            exchange(hp, idx, j)
            idx = j
    except Exception as exp:
        raise RuntimeError("Error en _sink") from exp
        
def _greater(heap: dict, elm1: any, elm2: any) -> bool: # Esto no es lo mismo que default compare? - Si :(
    """_greater compara dos elementos del montículo (heap) usando la función de comparación.

    Args:
        heap (dict): diccionario que representa el montículo (heap).
        elm1 (Any): primer elemento a comparar.
        elm2 (Any): segundo elemento a comparar.

    Returns:
        bool: True si elm1 > elm2, False en caso contrario.
    """
    try:
        _cmp = heap["cmp_function"]
        if _cmp(elm1, elm2) > 0:
            return True
        return False
    except Exception as exp:
        raise RuntimeError("Error en value_set") from exp
    

def exchange(heap, pos1, pos2): # Esta duncion la tenemos a cambio de insert
    try:
        al.exchange(heap["elements"], pos1, pos2)
    except Exception as exp:
        raise RuntimeError("Error en exchange")

def size(heap):
    try:
        return al.size(heap["elements"])
    except Exception as exp:
        raise RuntimeError("Error en el size")
    
def is_empty(heap):
    try:
        if size(heap) <= 0:
            return True
        return False
    except Exception as exp:
        raise RuntimeError("Error en is_empty")

def remove():
    pass

def get_first_prioroty(heap):
    pass
        

def is_present_value():
    pass

def ontains(): # que rayos ese nombre
    pass

def imporve_priority():
    pass
