from PACKET import Packet

class Queue:
    def __init__(self, id, ueid):   
        #print("---------------------------- Queue initialized")
        self.id             = id
        self.ueid           = ueid
        self.size           = 0
        self.packets        = []
        self.currentTime    = 0
    
    def getId(self):
        return self.id
    
    def getUeid(self):
        return self.ueid

    def getSize(self):
        return self.size

    def getPackets(self):
        return self.packets

    def getLastPacket(self):
        if len(self.packets) == 0:
            return 0
        else:
            return self.packets[-1]

    def getCurrentTime(self):
        return self.currentTime

    def setSize(self, new_size):
        self.size = new_size

    def enQueue(self, Packet):
        self.currentTime = Packet.getEnq_t()
        self.packets.append(Packet)
        self.size = self.size + 1

    def deQueue(self):
        self.packets.pop(0)

    def printEnq_t(self):
        if self.packets != 0:
            for item in self.packets:
                print("Uid:", item.getuId(),", Pid:", item.getpId(),", Enq_t:",item.getEnq_t())
        else:
            print("queue is empty")    




        

