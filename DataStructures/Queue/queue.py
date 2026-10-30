from DataStructures.List import single_linked_list as lt

def new_queue():
    return lt.new_list()
    
def enqueue(queue, element):
    return lt.add_last(queue, element)

def dequeue(queue):
    if not lt.is_empty(queue):
        return lt.remove_first(queue)
    raise Exception('EmptyStructureError: queue is empty')

def is_empty(queue)->bool:
    return lt.is_empty(queue)

def peek(queue):
    if not is_empty(queue):
        return lt.first_element(queue)
    raise Exception('EmptyStructureError: queue is empty')

def size(queue)->int:
    return queue["size"]

    
