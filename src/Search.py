from Vertex import Vertex
#import asyncio

def search():
    root = Vertex(3,3,0,0,True)
    steps=0
    capacity= (1,2)
    found_sol = False
    current = root
    visited = []
    queue = []
    queue.append(root)
    print(len(queue))
    while(len(queue)!=0 and not found_sol):             #main loop
        current = queue.pop(0)
        steps+=1
        hash = hash_func(current)
        current.print_vert()
        if hash in visited:     #checking if visited
            steps-=1
        else:
            visited.append(hash)#add to visited set
            if current.right.canibals==3 and current.right.canibals==3: #reached the end
                running=False
            else:
                if not game_over(current):
                    find_moves(current, capacity, queue)

    if found_sol:
        print("Found solution! Needed {0:d} steps to reach solution".format() )
    else:
        print("No solution found")

def hash_func(vertex):
    left_m = vertex.left.get_missionaries() << 7
    left_c = vertex.left.get_canibals() << 5
    right_m = vertex.right.get_missionaries() << 3
    right_c = vertex.right.get_canibals() << 1
    if vertex.left.get_boat():
        return left_m + left_c + right_m + right_c + 1 
    return left_m + left_c + right_m + right_c

def find_moves(vertex,capacity,queue):
    count=0
    left_m = vertex.left.get_missionaries()
    left_c = vertex.left.get_canibals()
    right_m = vertex.right.get_missionaries()
    right_c = vertex.right.get_canibals()
    boat_on_left = vertex.left.get_boat()
    if boat_on_left:
        #can take one or two people right?
        for i in capacity:
            if left_m>i:
                v = Vertex(left_m-i,left_c,right_m+i,right_c,False)
                if not game_over(v):
                    queue.append(v)
            if left_c>i:
                v= Vertex(left_m,left_c-i,right_m,right_c+i,False)
                if not game_over(v):
                    queue.append(v)
        if left_c>0 and left_m>0:
            v = Vertex(left_m-1,left_c-1,right_m+1,right_c+1,False)
            if not game_over(v):
                queue.append(v)
            
    else:
        #can take one or more people left?
        for i in capacity:
            if right_m>i:
                v = Vertex(left_m+i,left_c,right_m-i,right_c,True)
                if not game_over(v):
                    queue.append(v)
            if right_c>i:
                v= Vertex(left_m,left_c+i,right_m,right_c-i,True)
                if not game_over(v):
                    queue.append(v)
        if right_c>0 and right_m>0:
            v = Vertex(left_m+1,left_c+1,right_m-1,right_c-1,True)
            if not game_over(v):
                queue.append(v)
                
def game_over(vertex):
    
    return  (vertex.left.get_canibals() >vertex.left.get_missionaries()) or (vertex.right.get_canibals()  >vertex.right.get_missionaries())
    

search()
    