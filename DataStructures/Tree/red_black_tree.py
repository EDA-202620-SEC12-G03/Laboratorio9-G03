from DataStructures.List import array_list as al
from DataStructures.Tree import bst_node as bstn
from DataStructures.Tree import rbt_node as rbtn
from DataStructures.List import single_linked_list as sl
from typing import Any, Callable


RED = 0
BLACK = 1

def dflt_tree_node_cmp(key1: Any, key2: Any) -> int:
    """dflt_tree_node_cmp funcion de comparacion por defecto para los
    nodos de un árbol binario de búsqueda (BST).
    Args:
    key1 (Any): primera llave a comparar
    key2 (Any): segunda llave a comparar
    Returns:
    int: -1 si key1 < key2, 0 si key1 == key2, 1 si key1 > key2
    """
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1

def new_map() -> dict:
    """new_map _crea un nuevo mapa basado en un árbol binario de búsqueda (BST) y lo
    retorna.
    Returns:
    dict: diccionario que representa el árbol binario de búsqueda
    """
    try:
        # root: nodo raiz del árbol
        _new_bst = {
            "root": None}
        # retorna el árbol binario de búsqueda (BST)
        return _new_bst
    
    except Exception as exp:
        raise RuntimeError("Error en new_map") from exp

def put(tree:dict, key:Any, value:Any, cmp_func=dflt_tree_node_cmp):
    # agrega un nodo a un árbol vacio o no vacio
    try:
        # si el árbol no está vacío, inserta el nodo en la posición correcta
        
        tree["root"] = insert_node(tree["root"], key, value, cmp_func)
        rbtn.change_color(tree["root"], BLACK) # asegurarse de que la raíz sea negra
        return tree
    except Exception as exp:
        raise RuntimeError("Error en put") from exp

def insert_node(root, key:Any, value:Any, cmp_func):
    # inserta un nodo en la posición correcta del árbol
    try:
        if root is None:
            # caso base, si el arbol esta vacio o llego a una hoja
            root = rbtn.new_node(key, value)
        else:
            _cmp = cmp_func(key, root["key"])

            if _cmp < 0:
                # llave es menor, vamos a arbol izquierdo
                root["left"] = insert_node(root["left"], key, value, cmp_func)
            elif _cmp > 0:
                # llave es mayor, vamos a arbol derecho
                root["right"] = insert_node(root["right"], key, value, cmp_func)
            else:
                # llave ya existe, actualizamos el valor
                root["value"] = value

            # despues de insertar TENEMOS QUE RECOLOREAR
            
            
            if rbtn.is_red(root["right"]) and not rbtn.is_red(root["left"]):
                root = rotate_left(root)
            if rbtn.is_red(root["left"]) and rbtn.is_red(root["left"]["left"]):
                root = rotate_right(root)
            if rbtn.is_red(root["left"]) and rbtn.is_red(root["right"]):
                rbtn.flip_color(root)

        root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1

        return root

    except Exception as exp:
        raise RuntimeError("Error en insert_node") from exp

def rotate_left(node):
    # rotación izquierda para compenssar dos enlaces rojos consecutivos
    try:
        x = node["right"]
        node["right"] = x["left"]
        x["left"] = node
        x["color"] = x["left"]["color"]
        rbtn.change_color(x["left"], RED)
        x["size"] = node["size"]
        node["size"] = size_tree(node["left"]) + size_tree(node["right"]) + 1
        return x
    except Exception as exp:
        raise RuntimeError("Error en rotate left")

def rotate_right(node):
    # rotación izquierda para compenssar dos enlaces rojos consecutivos
    try:
        x = node["left"]
        node["left"] = x["right"]
        x["right"] = node
        x["color"] = x["right"]["color"]
        rbtn.change_color(x["right"], RED)
        x["size"] = node["size"]
        node["size"] = size_tree(node["left"]) + size_tree(node["right"]) + 1
        return x
    except Exception as exp:
        raise RuntimeError("Error en rotate right")

def get(tree: dict, k: Any, cmp_func=dflt_tree_node_cmp) -> dict:
    """get recupera un nodo del árbol binario de búsqueda (BST) y lo
    retorna…
    """
    try:
        _root = tree["root"]
        result = get_node(_root, k, cmp_func)
        if result is not None:
            return rbtn.get_value(result)
        return None
    except Exception as exp:
        raise RuntimeError("Error en get") from exp

def get_node(node: dict, k: Any, cmp_func: Callable) -> dict:
    """
    Args:
        node (dict): nodo actual del árbol
        k (Any): llave del nodo a recuperar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol

    Returns:
        dict: diccionario con el nodo recuperado
    """
    try:
        # caso base, el arbol esta vacio
        _node = None
        # caso base, el arbol no esta vacio
        if node is not None:
            _cmp = cmp_func(k, node["key"])
            # si el nodo es igual a la llave, retornar el nodo
            if _cmp == 0:
                _node = node
            # si el nodo es menor que la llave, buscar en el subarbol izquierdo
            elif _cmp < 0:
                _node = get_node(node["left"], k, cmp_func)
            # si el nodo es mayor que la llave, buscar en el subarbol derecho
            elif _cmp > 0:
                _node = get_node(node["right"], k, cmp_func)
        return _node
    except Exception as exp:
        raise RuntimeError("Error en _get") from exp

def contains(tree: dict, k: Any, cmp_func=dflt_tree_node_cmp) -> bool:
    # verifica si el árbol contiene un nodo con la llave k

    try:
        # _root = tree["root"]
        if get(tree, k, cmp_func) is not None:
            return True
        return False
    except Exception as exp:
        raise RuntimeError("Error en contains") from exp

def size(tree: dict) -> int:
    """size contador de nodos del árbol binario de búsqueda (BST) y retorna el tamaño del árbol.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)

    Returns:
        int: tamaño del árbol binario de búsqueda (BST)
    """
    try:
        return size_tree(tree["root"])
    except Exception as exp:
        raise RuntimeError("Error en size") from exp


def size_tree(node: dict) -> int:
    """size_tree funcion recursiva que cuenta los nodos del árbol binario de búsqueda (BST) y retorna el tamaño del árbol.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        int: tamaño del árbol binario de búsqueda (BST), por defecto 0. Ademas, recordar que el nodo BST por defecto es de tamaño 1
    """
    if node is None:
        return 0
    return node["size"]

def is_empty(tree:dict):
    try:
        if tree["root"] is None:
            return True
        return False
    except Exception as exp:
        raise RuntimeError("Error en is_empty") from exp


def key_set(tree: dict):
    # key_set retorna un conjunto de llaves del árbol binario de búsqueda (BST) en orden ascendente.
    try:
        _root = tree["root"]
        keys = sl.new_list()
        if _root is not None:
            
            keys = key_set_tree(_root, keys)
            
        else:
            return keys
        return keys
    except Exception as exp:
        raise RuntimeError("Error en key_set") from exp

def key_set_tree(root: dict, keys):
    # key_set_tree funcion recursiva que agrega las llaves del árbol binario de búsqueda (BST) al conjunto de llaves en orden ascendente.
    if root is not None:
        key_set_tree(root["left"], keys)
        sl.add_last(keys, root["key"])
        key_set_tree(root["right"], keys)
    return keys

def value_set(tree:dict):
    # value_set retorna un conjunto de valores del árbol binario de búsqueda (BST) en orden ascendente.
    try:
        _root = tree["root"]
        values = sl.new_list()
        if _root is not None:
            values = value_set_tree(_root, values)
        else:
            return values
        return values
    except Exception as exp:
        raise RuntimeError("Error en value_set") from exp

def value_set_tree(root: dict, values):
    # value_set_tree funcion recursiva que agrega los valores del árbol binario de búsqueda (BST) al conjunto de valores en orden ascendente.
    if root is not None:
        value_set_tree(root["left"], values)
        sl.add_last(values, root["value"])
        value_set_tree(root["right"], values)
    return values


def get_min(tree):
    # get_min retorna la llave mínima del árbol binario de búsqueda (BST).
    try:
        _min_node = get_min_node(tree["root"])
        if _min_node is not None:
            return _min_node["key"]
        return None
    except Exception as exp:
        raise RuntimeError("Error en get_min") from exp

def get_min_node(root):
    _min_ = root
    if root is not None:
        if root["left"] is None:
            _min_ = root
        else:
            _min_ = get_min_node(root["left"])
    return _min_

def get_max(tree):
    try:
        _max_node = get_max_node(tree["root"])
        if _max_node is not None:
            return _max_node["key"]
        return None
    except Exception as exp:
            raise RuntimeError("Error en get_max") from exp

def get_max_node(root):
    _max_ = root
    if root is not None:
        if root["right"] is None:
            _max_ = root
        else:
            _max_ = get_max_node(root["right"])
    return _max_

def height(tree):
    # Encuentra la altura del árbol
    try:
        return height_tree(tree["root"])
    except Exception as exp:
        raise RuntimeError("Error en height") from exp

def height_tree(root):
    if root is None:
        return 0
    else:
        left_h = height_tree(root["left"])
        right_h = height_tree(root["right"])
        return 1 + max(left_h, right_h)

def keys(tree, key1, key2, cmp_func=dflt_tree_node_cmp):
    try:
        _keys = sl.new_list()
        _keys = keys_range(tree["root"], key1, key2, cmp_func, _keys)
        return _keys
    except Exception as exp:
        raise RuntimeError("Error en keys") from exp

def keys_range(root, key1, key2, cmp_funct, keys):
    if root is not None:
        _cmp_low = cmp_funct(key1, root["key"])
        _cmp_high = cmp_funct(key2, root["key"])
        # verificamos que lado del árbol recorrer
        if _cmp_low < 0:
            keys_range(root["left"], key1, key2, cmp_funct, keys)
        if _cmp_low <= 0 and _cmp_high >= 0:
            sl.add_last(keys, root["key"])
        if _cmp_high > 0:
            keys_range(root["right"], key1, key2, cmp_funct, keys)
    return keys

def values(tree, key1, key2, cmp_func=dflt_tree_node_cmp):
    try:
        _values = sl.new_list()
        _values = values_range(tree["root"], key1, key2, cmp_func, _values)
        return _values
    except Exception as exp:
        raise RuntimeError("Error en keys") from exp

def values_range(root, key1, key2, cmp_funct, values):
    if root is not None:
        _cmp_low = cmp_funct(key1, root["key"])
        _cmp_high = cmp_funct(key2, root["key"])
        # verificamos que lado del árbol recorrer
        if _cmp_low < 0:
            values_range(root["left"], key1, key2, cmp_funct, values)
        if _cmp_low <= 0 and _cmp_high >= 0:
            sl.add_last(values, root["value"])
        if _cmp_high > 0:
            values_range(root["right"], key1, key2, cmp_funct, values)
    return values
