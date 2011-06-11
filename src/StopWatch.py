'''
Created on Jun 10, 2011

@author: BMAllred
'''
import time

class StopWatch(object):
    '''
    Stop watch object.
    '''

    def __init__(self):
        '''
        Initializes a new instance of the StopWatch class.
        '''
        
        self.StartTime = None
        self.StopTime = None
    
    def Start(self):
        self.StartTime = time.clock()
        self.StopTime = None
        
        return self.StartTime
    
    def Stop(self):
        self.StopTime = time.clock()
    
    def TimeElapsed(self):
        
        if self.StartTime is None:
            return -1
        elif self.StopTime is None:
            return time.clock() - self.StartTime
        
        return self.StopTime - self.StartTime
    
    def Reset(self):
        self.StartTime = None
        self.StopTime = None