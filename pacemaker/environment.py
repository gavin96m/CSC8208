from unittest import skip
import pacemaker

class Environment:     
    #Set the unit of time
    _unit_of_time = 0.1
    time = 0
    _length_of_simulation = int

    def __init__(self, length):
        self.pacemaker = pacemaker()
        self._length_of_simulation = length

    def is_finished(self):
        if self.time >= self._length_of_simulation:
            return True
        else:
            return False

    def get_time(self):
        """ Return current time """
        return(self.time)

    def advance_time(self):
        """ Basic use of advancing time """
        self.time += self._unit_of_time
        if(self.is_finished()):
            #TODO Add something to end simulation
            skip