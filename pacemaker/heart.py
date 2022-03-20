class Heart(object):

    # x: time ms / s, y: voltage mV / mm
    def __init__(self, heart_rate, atrial, ventricular, p_amplitude, qrs_height, st_level, t_amplitude,
                 p_time, pq_time, qrs_time, st_time, t_time):
        # interval = distance from R to R

        self.heart_rate = heart_rate
        self.atrial = atrial
        self.ventricular = ventricular
        self.p_amplitude = p_amplitude
        self.qrs_height = qrs_height
        self.st_level = st_level
        self.t_amplitude = t_amplitude
        self.p_time = p_time
        self.pq_time = pq_time
        self.qrs_time = qrs_time
        self.st_time = st_time
        self.t_time = t_time


@property  # getter
def heart_rate(self):
    return self.heart_rate

@heart_rate.setter
def heart_rate(self, heart_rate):
    self.heart_rate = heart_rate

@property  # getter
def atrial(self):
    return self.atrial

@atrial.setter
def heart_rate(self, atrial):
    self.atrial = atrial

@property  # getter
def ventricular(self):
    return ventricular

@ventricular.setter
def heart_rate(self, ventricular):
    self.ventricular = ventricular

@property  # getter
def p_amplitude(self):
    return self.p_amplitude

@p_amplitude.setter
def p_amplitude(self, p_amplitude):
    self.p_amplitude = p_amplitude

@property  # getter
def qrs_height(self):
    return self.qrs_height

@qrs_height.setter
def qrs_height(self, qrs_height):
    self.qrs_height = qrs_height

@property  # getter
def st_level(self):
    return self.st_level

@st_level.setter
def st_level(self, st_level):
    self.st_level = st_level

@property  # getter
def t_amplitude(self):
    return self.t_amplitude

@t_amplitude.setter
def t_amplitude(self, t_amplitude):
    self.t_amplitude = t_amplitude

@property  # getter
def p_time(self):
    return self.p_time

@p_time.setter
def p_time(self, p_time):
    self.p_time = p_time

@property  # getter
def pq_time(self):
    return self.pq_time

@pq_time.setter
def pq_time(self, pq_time):
    self.pq_time = pq_time

@property  # getter
def qrs_time(self):
    return self.qrs_time

@qrs_time.setter
def qrs_time(self, qrs_time):
    self.qrs_time = qrs_time

@property  # getter
def st_time(self):
    return self.st_time

@st_time.setter
def st_time(self, st_time):
    self.st_time = st_time

@property
def t_time(self):
    return self.T_time

@t_time.setter
def t_time(self, T_time):
    self.T_time = T_time