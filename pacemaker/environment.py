import pacemaker, accelerometer

class Environment:     
    #Set the unit of time
    unit_of_time = 0.1
    time = 0
    accelerometer = False
    def __init__(self):
        self.pacemaker = pacemaker()

    def is_finished(self):
        pass

    def add_accelerometer(self):
        """ Creates an accelerometer """
        self.accelerometer = accelerometer()

    def get_accelerometer(self):
        """ Returns the accelerometer """
        return(self.accelerometer)

    def get_time(self):
        """ Return current time """
        return(self.time)

    def advance_time(self):
        """ Basic use of advancing time """
        self.time += self.unit_of_time