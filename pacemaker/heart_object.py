class Heart(object):
    # x: time ms / s, y: voltage mV / mm
    def __init__(self, HeartRate, P_peak, Q, R, S, T, P_waves, QRS_waves, ST_up, T_wave,
                 P_time,P_peak_time, PR_time, QRS_time, ST_time, T_time, QT_time):
#interval = distance from R to R

        self.HeartRate = HeartRate
        self.P_peak = P_peak
        self.Q = Q
        self.R = R
        self.S = S
        self.T = T
        self.P_waves = P_waves
        self.QRS_waves = QRS_waves
        self.ST_up = ST_up
        self.T_wave = T_wave
        self.P_time = P_time
        self.P_peak_time = P_peak_time
        self.PR_time = PR_time
        self.QRS_time = QRS_time
        self.ST_time = ST_time
        self.T_time = T_time
        self.QT_time = QT_time

    @property  # getter
    def p_peak(self):
        return self.P_peak

    @p_peak.setter
    def p_peak(self, P_peak):
        self.P_peak = P_peak

    @property  # getter
    def q(self):
        return self.Q

    @q.setter
    def q(self, Q):
        self.Q = 1/4 * self.r

    @property  # getter
    def r(self):
        return self.R

    @r.setter
    def r(self, R):
        self.R = R

    @property  # getter
    def s(self):
        return self.S

    @s.setter
    def s(self, S):
        self.S = S

    @property  # getter
    def t(self):
        return self.T

    @t.setter
    def t(self, T):
        self.T = 1/10 * self.r

    @property  # getter
    def heart_rate(self):
        return self.HeartRate

    @heart_rate.setter
    def heart_rate(self, HeartRate):
        self.HeartRate=HeartRate

    @property  # getter
    def p_waves(self):
        return self.P_waves

    @p_waves.setter
    def p_waves(self, P_waves):
        self.P_waves = P_waves

    @property  # getter
    def qrs_waves(self):
        return self.QRS_waves

    @qrs_waves.setter
    def qrs_waves(self, QRS_waves):
        self.QRS_waves = QRS_waves

    @property  # getter
    def st_up(self):
        return self.ST_up

    @st_up.setter
    def st_up(self, ST_up):
        self.ST_up = ST_up

    @property  # getter
    def t_wave(self):
        return self.T_wave

    @t_wave.setter
    def t_wave(self, T_wave):
        self.T_wave = T_wave

    @property  # getter
    def p_time(self):
        return self.P_time

    @p_time.setter
    def p_time(self, P_time):
        self.P_time = P_time

    @property  # getter
    def p_peak_time(self):
        return self.P_peak_time

    @p_peak_time.setter
    def p_peak_time(self, P_peak_time):
        self.P_peak_time = 1 / 2 * self.p_time

    @property  # getter
    def pr_time(self):
        return self.PR_time

    @pr_time.setter
    def pr_time(self, PR_time):
        self.PR_time = PR_time

    @property  # getter
    def qrs_time(self):
        return self.QRS_time

    @qrs_time.setter
    def qrs_time(self, QRS_time):
        self.QRS_time = QRS_time

    @property  # getter
    def st_time(self):
        return self.ST_time

    @st_time.setter
    def st_time(self, ST_time):
        self.ST_time = ST_time

    @property
    def t_time(self):
        return self.T_time

    @t_time.setter
    def t_time(self, T_time):
        self.T_time = T_time

    @property  # getter
    def qt_time(self):
        return self.QT_time

    @qt_time.setter
    def qt_time(self, QT_time):
        self.QT_time = QT_time

    def heart_info(self):
        info = [self.HeartRate, self.P_waves, self.QRS_waves]
        return info

    def amp_info(self):
        info = [self.p, self.q, self.r, self.s, self.t, self.P_waves, self.QRS_waves, self.st_up, self.t_wave]
        return info

    def time_info(self):
        info = [self.p_time,self.p_peak_time, self.qrs_time, self.st_time,self.pr_time, self.t_time,self.qt_time]
        return info

    def heart_arr(self):
        print("file")
        f = open("../heart_info", "r")
        heart_file = []
        print("read")
        for line in f.readlines():
            cur_line = line.strip().split(" ")
            heart_file.append(cur_line[:])
        print(heart_file)
        return heart_file

    def heart_output(self):
        print("file")
        f = open("../heart_output", "r")
        heart_file = []
        print("read")
        for line in f.readlines():
            cur_line = line.strip().split(" ")
            heart_file.append(cur_line[:])
        print(heart_file)
        return heart_file


def main():

    # right Heart Value
    ecg_t_info = Heart.heart_info
    # print("file content")
    # Heart.heart_arr(Heart)

if __name__ == '__main__':
    main()