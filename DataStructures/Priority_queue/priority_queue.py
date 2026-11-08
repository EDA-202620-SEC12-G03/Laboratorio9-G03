from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import array_list as al


def default_compare_lower_value(father_node, child_node):
    # Retorna True si el padre tiene MAYOR valor (rompe el Min-Heap) y debe intercambiarse
    return pqe.get_priority(father_node) > pqe.get_priority(child_node)

def default_compare_higher_value(father_node, child_node):
    # Retorna True si el padre tiene MENOR valor (rompe el Max-Heap) y debe intercambiarse
    return pqe.get_priority(father_node) < pqe.get_priority(child_node)

def default_compare_function(value, pq_node):
    """Compara entre el valor de un nodo de la lista y un valor especifico

    Args:
        pq_node (dict): nodo de la lista
        value (any): valor que se quiere comparar, o una entrada de la cola
    """
    if isinstance(value, dict):
        value = pqe.get_value(value)
    node_value = pqe.get_value(pq_node)
    if value > node_value:
        return 1
    if value < node_value:
        return -1
    else:
        return 0

def should_swap(my_heap, parent, child):
    """Devuelve True si el par (padre, hijo) rompe la condición del heap."""
    try:
        return my_heap["cmp_function"](parent, child)
    except Exception as exp:
        raise RuntimeError("Error en priority") from exp

def new_heap(is_min_pq=True):
    cmp_function = default_compare_lower_value if is_min_pq else default_compare_higher_value
    heap = {
        'elements': al.new_list(),
        'size': 0,
        'cmp_function': cmp_function
    }
    return heap

def swim(heap: dict, idx: int) -> None:
    try:     
        while idx > 0:
            parent_idx = (idx - 1) // 2
            _parent = al.get_element(heap["elements"], parent_idx)
            _element = al.get_element(heap["elements"], idx)
            
            # Intercambia si se rompe la propiedad del heap
            if should_swap(heap, _parent, _element):
                exchange(heap, parent_idx, idx)
                idx = parent_idx
            else:
                break
    except Exception as exp:
        raise RuntimeError("Error en swim") from exp

def insert(heap, priority, value):
    try:
        lista = heap["elements"]
        node = pqe.new_pq_entry(priority, value)
        al.add_last(lista, node)
        heap["size"] += 1
        swim(heap, size(heap) - 1)
        return heap
    except Exception as exp:
        raise RuntimeError("Error en insert") from exp

def sink(hp: dict, idx: int) -> None:
    try:
        _size = hp["size"]
        while 2 * idx + 1 < _size:
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2
            target_child = left_child

            # Seleccionar el hijo prioritario para comparar/intercambiar
            if right_child < _size:
                _elm_left = al.get_element(hp["elements"], left_child)
                _elm_right = al.get_element(hp["elements"], right_child)
                if should_swap(hp, _elm_left, _elm_right):
                    target_child = right_child

            _parent = al.get_element(hp["elements"], idx)
            _child = al.get_element(hp["elements"], target_child)

            if should_swap(hp, _parent, _child):
                exchange(hp, idx, target_child)
                idx = target_child
            else:
                break
    except Exception as exp:
        raise RuntimeError("Error en sink") from exp

def exchange(heap, pos1, pos2):
    try:
        al.exchange(heap["elements"], pos1, pos2)
    except Exception as exp:
        raise RuntimeError("Error en exchange") from exp

def size(heap):
    try:
        return al.size(heap["elements"])
    except Exception as exp:
        raise RuntimeError("Error en el size") from exp

def is_empty(heap):
    try:
        return size(heap) <= 0
    except Exception as exp:
        raise RuntimeError("Error en is_empty") from exp

def remove(heap):
    try:
        if is_empty(heap):
            return None
        root = al.get_element(heap["elements"], 0)
        last = al.get_element(heap["elements"], size(heap) - 1)
        al.change_info(heap["elements"], 0, last)
        al.remove_last(heap["elements"])
        heap["size"] -= 1
        
        if not is_empty(heap):
            sink(heap, 0)
            
        return pqe.get_value(root)
    except Exception as exp:
        raise RuntimeError("Error en remove") from exp

def get_first_priority(heap):
    try:
        if is_empty(heap):
            return None
        return pqe.get_value(al.get_element(heap["elements"], 0))
    except Exception as exp:
        raise RuntimeError("Error en get_first_priority") from exp

def is_present_value(heap, value):
    """Revisa si un valor especifico existe dentro del heap

    Args:
        heap (dict): el heap que estas revisando
        value (any): el valor que quieres buscar

    Raises:
        RuntimeError: puede ser un problema de tipos de dato

    Returns:
        _type_: Retorna la posicion (comenzando en 1) si existe, si no, -1
    """
    try:
        pos = al.is_present(heap["elements"], value, default_compare_function)
        return pos + 1 if pos != -1 else -1
    except Exception as exp:
        raise RuntimeError("Error en is_present_value") from exp

def contains(heap, value):
    # Esta funcion devuelve un booleano
    try:
        return is_present_value(heap, value) != -1
    except Exception as exp:
        raise RuntimeError("Error en contains") from exp

def improve_priority(heap, new_priority, value):
    pos = is_present_value(heap, value)
    if pos == -1:
        return heap
    pos -= 1
    elemen = al.get_element(heap["elements"], pos)
    old_priority = pqe.get_priority(elemen)
    
    pqe.set_priority(elemen, new_priority)
    
    # Reorganizar el elemento según si la prioridad subió o bajó
    swim(heap, pos)
    sink(heap, pos)
    return heap
