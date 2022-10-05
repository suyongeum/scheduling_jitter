
class Packet:
    def __init__(self, pid, uid, init_t, size):   
        # print("---------------------------- Packet initialized")
        self.pid       = pid
        self.uid       = uid
        self.enq_t     = init_t
        self.deq_t     = 0
        self.arrv_t    = 0
        self.length    = size
        self.is_served = False
        self.RB_id     = [0, 0] # s_id # rb_id

    def setEnq_t(self, enq_t):
        self.enq_t = enq_t

    def setDeq_t(self, deq_t):
        self.deq_t = deq_t

    def setArrv_t(self, arrv_t):
        self.arrv_t = arrv_t

    def setState(self, state):
        self.is_served = state

    def setRB_id(self, s_id, rb_id):
        self.RB_id[0] = s_id
        self.RB_id[1] = rb_id

    def getpId(self):
        return self.pid
    
    def getuId(self):
        return self.uid

    def getEnq_t(self):
        return self.enq_t

    def getRB_id(self):
        return self.RB_id

    

    

