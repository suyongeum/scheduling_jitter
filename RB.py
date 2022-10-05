
class Rb:
    def __init__(self, id):   
        #print("---------------------------- Rb initialized")
        self.ID = id
        self.num_col_slots   = 10 # default value 10 slots within 1 frame
        self.num_row_RBs     = 25 # default value 25 RBs 
        self.uplink_slot_ids = [3, 4, 8, 9]

        self.RBmap = {}
        for slot_id in self.uplink_slot_ids:
            self.RBmap[slot_id] = [0] * self.num_row_RBs

    def getRBmap(self):
        return self.RBmap



