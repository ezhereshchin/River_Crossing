#from Vertex import Vertex
#import asyncio

def search():
    root =[3,3,0,0,0,0]
    steps=0
    capacity= (1,2)
    found_sol = False
    visited = []
    queue = []
    queue.append(root)
    while(len(queue)!=0 and not found_sol):             #main loop
        current = queue.pop(0)
        hash = hash_func(current)
        if hash in visited:     #checking if visited
            continue
        else:
#            print(current)

            visited.append(hash)#add to visited set
            if current[3]==3 and current[2]==3: #reached the end
                found_sol=True
            else:
 #               if not game_over(current):
                find_moves(current, capacity, queue)
        
    if found_sol:
        while(current!=root):
            steps+=1
            current=current[5]
            
        print("Found solution! Needed {0:d} steps to reach solution.".format(steps) )
    else:
        print("No solution found")

def hash_func(vertex):
    left_m = vertex[0] << 7
    left_c = vertex[1] << 5
    right_m = vertex[2] << 3
    right_c = vertex[3] << 1
    if vertex[4]==0:
        return left_m + left_c + right_m + right_c + 1 
    return left_m + left_c + right_m + right_c

def find_moves(vertex,capacity,queue):
    count=0
    left_m = vertex[0]
    left_c = vertex[1]
    right_m = vertex[2]
    right_c = vertex[3]
    boat_on_left = vertex[4]==0
    if boat_on_left:
        #can take one or two people right?
        for i in capacity:
            if left_m>=i:
                v = [left_m-i,left_c,right_m+i,right_c,1,vertex]
                if not game_over(v):
                    queue.append(v)
            if left_c>=i:
                v= [left_m,left_c-i,right_m,right_c+i,1,vertex]
                if not game_over(v):
                    queue.append(v)
        if left_c>0 and left_m>0:
            v = [left_m-1,left_c-1,right_m+1,right_c+1,1,vertex]
            if not game_over(v):
                queue.append(v)
            
    else:
        #can take one or more people left?
        for i in capacity:
            if right_m>=i:
                v = [left_m+i,left_c,right_m-i,right_c,0,vertex]
                if not game_over(v):
                    queue.append(v)
            if right_c>=i:
                v= [left_m,left_c+i,right_m,right_c-i,0,vertex]
                if not game_over(v):
                    queue.append(v)
        if right_c>0 and right_m>0:
            v = [left_m+1,left_c+1,right_m-1,right_c-1,0,vertex]
            if not game_over(v):
                queue.append(v)
                
def game_over(vertex):
    
    return  ((vertex[1] > vertex[0]) and vertex[0]!=0) or ((vertex[3] > vertex[2]) and vertex[2]!=0)
    

search()
    