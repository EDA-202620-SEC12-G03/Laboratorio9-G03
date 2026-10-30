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
    
def insert(heap, priority, value):
    heap["size"] += 1
    al.insert_element(heap["elements"], value, heap["size"] - 1)
    swim(heap, heapp["size"] - 1)
    return heap
    
def size(heap):
    return heap['size']
    
    
def is_empty(heap):
    return size(heap) == 0



