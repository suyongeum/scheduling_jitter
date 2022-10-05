from UE import Ue
from QUEUE import Queue
from PACKET import Packet
from RB import Rb
from SCHEDULER import Scheduler
from TRAFFICGENERATOR import TrafficGenerator

import logging

if __name__ == '__main__':  
    
    # Q   = Queue(1, 1)
    # TG  = TrafficGenerator(2, 1)
    # UE1 = Ue(1, 10, Q, TG)
    # P   = Packet(1, 0.2, 2)
    # RB  = Rb(1)
    # SCH = Scheduler([UE1])
    
    # print(TG.poissonInterArrvalGen())

    mylogger = logging.getLogger("EUM")
    mylogger.setLevel(logging.DEBUG)
    #mylogger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    mylogger.addHandler(console)

    #############################
    # Number of UEs
    UE_IDs                 = [0, 1, 2]
    transmission_rate      = [1, 1, 1]
    poission_arrival_rate  = [2, 2, 2] # how many packets per unit time

    # Number of Queues per UE
    queueid           = 0       # We assum there is only one queue per UE

    ###################
    # Define UE objects
    UEs = []
    for ueid, tr, traffic_arrival_rate in zip(UE_IDs, transmission_rate, poission_arrival_rate):
        
        Q  = Queue(queueid, ueid)     
        seed = ueid 
        TG = TrafficGenerator(traffic_arrival_rate, seed)

        UEs.append(Ue(ueid, tr, Q, TG))

    ###################
    # Define Schedule object
    SCHD = Scheduler()

    #############################################################################################
    # Simulation Start
    num_frames = 1                  # 10 ms
    num_slots  = 5 * num_frames    # num_slots
    current_time      = 0.0
    scheduling_begin  = False

    # Simulation start
    for current_slot_time in range(1, num_slots):

        mylogger.info("\n ########################## Scheduling begins at Slot: %d", current_slot_time)
              
        # Keep generating packets in each UE 
        # until the enqueue time of the last packet at each UE  
        # becomes more than the scheduling event time
        for UE_obj in UEs:
            while True:
                UE_obj.packet_generation()
                if UE_obj.get_lastEnqueue_time() >= current_slot_time:
                    break
        
        # BSR report...
        # The reported packets in the queues 
        # (packets arrived before the scheduling event) are emptied
        # Then, the non-reported packets are remained in the queue. 
        # We assume that the reported packets will be served successfully.
        for UE_obj in UEs:
            queue = UE_obj.get_queue()
            # This line prints all packets in the queue
            # UE_obj.get_queue().printEnq_t()
            # This code empties the queue and transmit the data to the base station.
            SCHD.transmit_BSR(queue, current_slot_time)

        print("\n ------------ BSR report: the reported packets for scheduling")
        for q_obj in SCHD.getBSR():
            q_obj.printEnq_t()
        
        print("\n ------------ Resource Map before scheduling")
        SCHD.printResourceMap(current_slot_time)

        print("\n ------------ Resource Map after scheduling")
        SCHD.beginScheduling(current_slot_time)
            

        # print("\n ------------------------ Current Q status after transmission")
        # for UE_obj in UEs:
        #     queue = UE_obj.get_queue()
        #     UE_obj.get_queue().printEnq_t()





  
        