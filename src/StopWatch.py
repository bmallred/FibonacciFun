'''
Created on Jun 10, 2011

@author: BMAllred
'''
import datetime

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
    
    def Reset(self):
        '''
        Reset stop watch.
        '''
        
        self.StartTime = None
        self.StopTime = None
        
    def Start(self):
        '''
        Start a new stop watch.
        '''
        
        self.StartTime = datetime.datetime.now()
        self.StopTime = None
        
        return self.StartTime
    
    def Stop(self):
        '''
        Stop recording the time.
        '''
        
        self.StopTime = datetime.datetime.now()
    
    def TimeElapsed(self):
        '''
        Returns the time elapsed.
        '''
        
        if self.StartTime is None:
            return -1
        elif self.StopTime is None:
            return datetime.datetime.now() - self.StartTime
        
        return self.StopTime - self.StartTime
    
    def TotalSeconds(self):
        '''
        Returns the total seconds elapsed.
        '''
        
        return self.TimeElapsed().seconds
    
    def TotalMilliseconds(self):
        '''
        Returns the total milliseconds elapsed.
        '''
        
        return self.TimeElapsed().microseconds / 1000