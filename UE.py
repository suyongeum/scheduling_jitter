from QUEUE import Queue
from PACKET import Packet
from TRAFFICGENERATOR import TrafficGenerator
import random

#######################################################################################
# 
class Ue:
    def __init__(self, uid, tr, Queue, TrafficGenerator):
        #print("---------------------------- Ue initialized")
        self.uid = uid
        self.TR = tr                # Transmission Rate requirement
        self.isActive = False       
        self.q = Queue              # Queue object
        self.TG = TrafficGenerator  # Traffic Generator object
        self.packetId = 0           # Packet ID
        
    def getId(self):
        return self.ID
    
    def getTr(self):
        return self.TR

    def getTg(self):
        return self.TG
    
    def get_state(self):
        return self.isActive

    def get_queue(self):
        return self.q

    def get_lastEnqueue_time(self):
        return self.q.getCurrentTime()
    
    def set_state(self, new_state):
        self.isActive = new_state

    def packet_generation(self):
        
        # constant packet size = 1
        packet_size = 1

        # Packet generation
        self.TG.setSeed(random.randint(0,1000))
        #self.TG.setSeed(1)
        interarrival_time = self.TG.poissonInterArrvalGen()

        # Calculate the absolute time
        last_time_packet = self.q.getCurrentTime()#p_item.getEnq_t()
        current_time     = last_time_packet + interarrival_time      

        one_packet = Packet(self.packetId, self.uid, current_time, packet_size)

        self.packetId = self.packetId + 1

        # Packet goes into the queue
        self.q.enQueue(one_packet)

        
        


    
