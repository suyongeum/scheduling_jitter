import random
import math
import numpy as np

class TrafficGenerator:
    def __init__(self, lambda_, seed):   
        #print("---------------------------- TrafficGenerator initialized")
        self.lambda_ = lambda_
        self.seed    = seed

    def poissonIntGen(self, mean, num_gen):
        rng     = np.random.default_rng(); 
        int_arr = rng.poisson(mean, num_gen)
        return int_arr

    def poissonInterArrvalGen(self):
        #Get the next probability value from Uniform(0,1)
        random.seed(self.seed)
        p = random.random()
        #Plug it into the inverse of the CDF of Exponential(_lamnbda)
        _inter_arrival_time = -1.0 * math.log(1.0 - p)/self.lambda_
        #Add the inter-arrival time to the running sum
        #_arrival_time = _arrival_time + _inter_arrival_time

        return _inter_arrival_time

    def setLambda(self, lambda_):
        self.lambda_ = lambda_

    def setSeed(self, seed_):
        self.seed = seed_


    

