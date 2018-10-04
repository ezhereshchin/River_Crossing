
class Vertex():

    def __init__(self,left_mis,left_can,left_mis,right_mis,right_can):
        self.left = Left(left_mis,left_can)
        self.right = Right(right_mis,right_can)
        return
    
    
class Left():
    canibals = 0
    missionaries = 0
    
    def __init__(self,mis,can):
        self.canibals = can
        self.missionaries = mis
        return
    
class Right():
    canibals = 0
    missionaries = 0
    
    def __init__(self,mis,can):
        self.canibals = can
        self.missionaries = mis
        return
    