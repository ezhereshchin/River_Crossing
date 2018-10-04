
class Vertex():

    def __init__(self,left_mis,left_can,left_mis,right_mis,right_can, boat_on_left):
       
        self.left = Side(left_mis, left_can, boat_on_left)
        self.right = Side(right_mis, right_can, not boat_on_left)

        return
    
    


class Side():
    canibals = 0
    missionaries = 0
    boat = False    
    
    def __init__(self,mis,can,boat):
        self.canibals = can
        self.missionaries = mis
        self.boat=boat
        return
    
    def get_canibals(self):
        return self.canibals
    
    def get_missionaries(self):
        return self.missionaries
    
    def get_boat(self):
        return boat
    