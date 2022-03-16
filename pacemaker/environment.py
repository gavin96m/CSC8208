from time import sleep
from unittest import skip
import pacemaker

class Environment:     
    #Set the unit of time
    _unit_of_time = 0.1
    time = 0
    _length_of_simulation = int
    #Set how many times faster than real time it should be
    _sim_speed = 4

    def __init__(self, length):
        self.pacemaker = pacemaker.Pacemaker()
        self._length_of_simulation = length

        while(not self.is_finished()):
            sleep(self._unit_of_time / self._sim_speed)
            self.pacemaker.advance()
            self.advance_time()
            print(self.get_time())

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


if __name__ == '__main__':
    environment = Environment(1000)
