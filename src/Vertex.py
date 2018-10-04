
class Vertex():

    def __init__(self,left_mis,left_can,left_mis,right_mis,right_can, boat_on_left):
       
        if boat_on_left:
            self.left = Left(left_mis,left_can,True)
            self.right = Right(right_mis,right_can,False)
        else:
             self.left = Left(left_mis,left_can,False)
             self.right = Right(right_mis,right_can,True)
        return
    
    
class Left():
    canibals = 0
    missionaries = 0
    boat = False    
    
    def __init__(self,mis,can,boat):
        self.canibals = can
        self.missionaries = mis
        self.boat=True
        return
    
class Right():
    canibals = 0
    missionaries = 0
    boat = False
    def __init__(self,mis,can,boat):
        self.canibals = can
        self.missionaries = mis
        return
