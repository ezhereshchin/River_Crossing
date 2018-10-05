
class Vertex():

    def __init__(self, left_mis, left_can, right_mis, right_can, boat_on_left):
       
        self.left = Side(left_mis, left_can, boat_on_left)
        self.right = Side(right_mis, right_can, not boat_on_left)

        return
    
    def print_vert(self):
        if self.left.boat:
            print("({}M {}C B|{}M {}C)".format(self.left.missionaries,self.left.canibals,self.right.missionaries,self.right.canibals))
        else:
            print("({}M {}C|B {}M {}C)".format(self.left.missionaries,self.left.canibals,self.right.missionaries,self.right.canibals))


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
        return self.boat
    