# @Time    : 2022-03-12 1:55 a.m.
# @Author  : Xiaoxia Li
# @FileName: test.py
# @Software: PyCharm

class ECG(object):
    # x: time ms / s, y: voltage mV / mm
    def __init__(self, HeartRate, AtrialAmplitude, VenAmplitude, AtrialPulseWidth,
                 VentricularPulseWidth, P_waves, QRS_waves, ST_up, T_wave,
                 P_time, PR_time, QRS_time, ST_time, T_time, QT_time):
        self.HeartRate = HeartRate
        self.AtrialAmplitude = AtrialAmplitude
        self.VenAmplitude = VenAmplitude
        self.AtrialPulseWidth = AtrialPulseWidth
        self.VentricularPulseWidth = VentricularPulseWidth
        self.P_waves=P_waves
        self.QRS_waves = QRS_waves
        self.ST_up = ST_up
        self.T_wave = T_wave
        self.P_time = P_time
        self.PR_time = PR_time
        self.QRS_time = QRS_time
        self.ST_time = ST_time
        self.T_time = T_time
        self.QT_time = QT_time

    @property  # getter
    def heart_rate(self):
        return self.HeartRate

    @heart_rate.setter
    def heart_rate(self, HeartRate):
        pass

    @property # getter
    def atrial_amplitude(self):
        return self.AtrialAmplitude

    @atrial_amplitude.setter
    def atrial_amplitude(self, AtrialAmplitude):
        self.AtrialAmplitude = AtrialAmplitude

    @property  # getter
    def ventricualr_amplitude(self):
        return self.VenAmplitude

    @ventricualr_amplitude.setter
    def ventricualr_amplitude(self, VenAmplitude):
        self.VenAmplitude = VenAmplitude

    @property # getter
    def atrial_pulse_width(self):
        return self.AtrialPulseWidth

    @atrial_pulse_width.setter
    def atrial_pulse_width(self, AtrialPulseWidth):
        self.AtrialPulseWidth = AtrialPulseWidth

    @property  # getter
    def ventricular_pulse_width(self):
        return self.VentricularPulseWidth

    @ventricular_pulse_width.setter
    def ventricular_pulse_width(self, VentricularPulseWidth):
        self.VentricularPulseWidth = VentricularPulseWidth

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

    @property# getter
    def qt_time(self):
        return self.QT_time

    @qt_time.setter
    def qt_time(self, QT_time):
        self.QT_time = QT_time

    def ecg_dic(self):
        ecg_dic={"HeartRate": self.HeartRate, "AtrialAmplitude": self.AtrialAmplitude,
                 "VenAmplitude": self.VenAmplitude, "AtrialPulseWidth": self.AtrialPulseWidth,
                 "VentricularPulseWidth": self.VentricularPulseWidth, "s P_waves": self.P_waves,
                 "ST_up": self.ST_up, "QRS_waves": self.QRS_waves, "T_wave": self.T_wave,
                 "P_time": self.P_time, "PR_time": self.PR_time, "QRS_time": self.QRS_time,
                 "ST_time": self.ST_time, "T_time": self.T_time, "QT_time": self.QT_time}
        return ecg_dic

def main():
    # right ECG Value
    ecg_t_info = ECG(70, 5, 5, 0.5, 0.8,
                     0.12, 1.0, 1.6, 0.6,
                     0.12, 0.13, 0.08, 0.09, 0.2, 0.43)
    print(ecg_t_info.ecg_dic())

    # Wrong ECG Value
    ecg_f_info = ECG(40, 5, 5, 0.5, 0.8,
                     0.22, 1.5, 2.6, 0.25,
                     0.14, 0.22, 0.13, 0.18, 0.27, 0.5)
    print(ecg_f_info.ecg_dic())
    print("Heart Rate: ", ecg_f_info.ecg_dic()["HeartRate"])

if __name__  == '__main__':
    main()