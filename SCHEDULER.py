import copy
from QUEUE import Queue
from RB import Rb

class Scheduler:
    def __init__(self):   
        #print("---------------------------- Scheduler initialized")
        self.BSR         = []
        self.RBs         = []
   
    def transmit_BSR(self, queue, current_slot_time):

        BSR = copy.deepcopy(queue)
      
        # Empty the Queue
        for item in queue.getPackets().copy():
            if item.getEnq_t() < current_slot_time:
                queue.getPackets().remove(item)    

        # Transmit the BSR to the base station
        for item in BSR.getPackets().copy():
            if item.getEnq_t() > current_slot_time:
                BSR.getPackets().remove(item) 

        self.BSR.append(BSR)

    def getBSR(self):
        return self.BSR

    def beginScheduling(self, current_slot_time):

        # Packets in the Buffer State Report
        for queue in self.BSR:
            #print(queue.getUeid())
            uid = queue.getUeid()
            for packet in queue.getPackets():
                #print(packet.getpId())
                pid = packet.getpId()
        
        # Resource Block
        # one_RB = Rb(current_slot_time)
        # for key, value in one_RB.getRBmap().items():
        #     print(key, value)

        self.printResourceMap(current_slot_time)
        
        # Empty self.BSR
        self.BSR = []

    def printResourceMap(self, current_slot_time):        
        # Resource Block
        one_RB = Rb(current_slot_time)
        for key, value in one_RB.getRBmap().items():
            print("s_id:", key, value)


