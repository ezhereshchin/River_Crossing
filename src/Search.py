from Vertex import Vertex
class Search():
    root = Vertex(3,3,0,0,True)
    capacity= (1,2)
    running = True
    current = root
    previous = root
    visited = []
    queue = LinkedList.Queue()
    while(running):             #main loop
        hash = hash_func(current)
        if hash in visited:     #checking if visited
            current = previous  #backtracking
            continue 
        else:
            visited.append(hash)#add to visited set
            if current.right.canibals==3 and current.right.canibals==3: #reached the end
                running=False
            else:
                find_moves(current,queue)
        
            
def hash_func():
    return "blah"

def find_moves(vetex,capacity,queue):
    count=0
    left_m = vertex.left.get_missionaries()
    left_c = vertex.left.get_caniblas()
    right_m = vertex.right.get_missionaries()
    right_c = vertex.right.get_missionaries()
    boat_on_left = vertex.left.get_boat()
    if vertex.left.boat:
        #can take one or two people right?
        for c in capacity:
            if 
    else:
        #can take one or more people left?
            