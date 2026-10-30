from DataStructures.List import single_linked_list as lt

def new_stack():
    return lt.new_list()

def push(stack, element):
    return lt.add_first(stack, element)

def pop(stack):
    if not lt.is_empty(stack):
        return lt.remove_first(stack)
    raise Exception("EmptyStructureError: stack is empty")

def is_empty(stack):
    return lt.is_empty(stack)

def top(stack):
    if not is_empty(stack):
        return lt.get_element(stack, 0)
    raise Exception('EmptyStructureError: stack is empty')

def size(stack):
    return lt.size(stack)