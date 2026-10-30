from DataStructures.Priority_queue import pq_entry as pe
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import array_list as al

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def new_heap(is_min_pq=True):
    cmp_function = default_compare_lower_value
    if is_min_pq:
        cmp_function = default_compare_lower_value
    heap = {
    'elements': None,
    'size': 0,
    'cmp_function': cmp_function
    }
    
    heap['elements'] = al.new_list()
    
    return heap
    
def swim(heap: dict, idx: int) -> None:
    """_swim hace "swim", "sube" o "flota" "bottom-up reheapfy" el elemento en la posición idx del montículo (heap).

    Args:
        heap (dict): diccionario que representa el montículo (heap).
        idx (int): índice del elemento a hacer "swim".
    """
# aqui había un try
    while idx > 0:
            _parent = al.get_element(heap["elements"], idx // 2)
            _element = al.get_element(heap["elements"], idx)
            if _greater(heap, _parent, _element):
                _exchange(heap, idx, idx // 2)
            idx = idx // 2
#aqui había un except
        err("heap", "_swim()", exp)
        
def _sink(hp: dict, idx: int) -> None:
    """_sink hace "sink", "baja" o "hundir" "top-down reheapfy" el elemento en la posición idx del montículo (heap).

    Args:
        hp (dict): diccionario que representa el montículo (heap).
        idx (int): índice del elemento a hacer "sink".
    """
#aquí había un try
        _size = hp["size"]
        while 2 * idx < _size:
            j = 2 * idx
            if j < _size:
                _elm1 = arlt.get_element(hp["elements"], j)
                _elm2 = arlt.get_element(hp["elements"], j + 1)
                if _greater(hp, _elm1, _elm2):
                    j += 1
            _elm1 = arlt.get_element(hp["elements"], idx)
            _elm2 = arlt.get_element(hp["elements"], j)
            if not _greater(hp, _elm1, _elm2):
                break
            _exchange(hp, idx, j)
            idx = j
#aquí había un except
        err("heap", "_sink()", exp)
        
def _greater(heap: dict, elm1: Any, elm2: Any) -> bool:
    """_greater compara dos elementos del montículo (heap) usando la función de comparación.

    Args:
        heap (dict): diccionario que representa el montículo (heap).
        elm1 (Any): primer elemento a comparar.
        elm2 (Any): segundo elemento a comparar.

    Returns:
        bool: True si elm1 > elm2, False en caso contrario.
    """
# aqui había un try
        _cmp = heap["cmp_function"]
        if _cmp(elm1, elm2) > 0:
            return True
        return False
# aquí había un except
        err("heap", "_greater()", exp)
