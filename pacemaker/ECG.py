#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ECG:
    # Constructor
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
    
    #define setter and getter for each parameter
    
    def get_heart_rate(self):
        return self.HeartRate

    def set_heart_rate(self, HeartRate):
        self.HeartRate = HeartRate

    def get_atrial_amplitude(self):
        return self.AtrialAmplitude

    def set_atrial_amplitude(self, AtrialAmplitude):
        self.AtrialAmplitude = AtrialAmplitude

    def get_ventricualr_amplitude(self):
        return self.VenAmplitude

    def set_ventricualr_amplitude(self, VenAmplitude):
        self.VenAmplitude = VenAmplitude

    def get_atrial_pulse_width(self):
        return self.AtrialPulseWidth

    def set_atrial_pulse_width(self, AtrialPulseWidth):
        self.AtrialPulseWidth = AtrialPulseWidth

    def get_ventricular_pulse_width(self):
        return self.VentricularPulseWidth

    def set_ventricular_pulse_width(self, VentricularPulseWidth):
        self.VentricularPulseWidth = VentricularPulseWidth

    def get_p_waves(self):
        return self.P_waves

    def set_p_waves(self, P_waves):
        self.P_waves = P_waves

    def get_qrs_waves(self):
        return self.QRS_waves

    def set_qrs_waves(self, QRS_waves):
        self.QRS_waves = QRS_waves

    def get_st_up(self):
        return self.ST_up

    def set_st_up(self, ST_up):
        self.ST_up = ST_up

    def get_t_wave(self):
        return self.T_wave

    def set_t_wave(self, T_wave):
        self.T_wave = T_wave

    def get_p_time(self):
        return self.P_time

    def set_p_time(self, P_time):
        self.P_time = P_time

    def get_pr_time(self):
        return self.PR_time

    def set_pr_time(self, PR_time):
        self.PR_time = PR_time

    def get_qrs_time(self):
        return self.QRS_time

    def set_qrs_time(self, QRS_time):
        self.QRS_time = QRS_time

    def get_st_time(self):
        return self.ST_time

    def set_st_time(self, ST_time):
        self.ST_time = ST_time

    def get_t_time(self):
        return self.T_time
    
    def set_t_time(self, T_time):
        self.T_time = T_time


# In[2]:


#take an object from ECG class with the right data

ecg_right = ECG(70, 5, 5, 0.5, 0.8,0.12, 1.0, 1.6, 0.6,0.12, 0.13, 0.08, 0.09, 0.2, 0.43)


# In[3]:


#take an object from ECG class with the wrong data

ecg_wrong = ECG(40, 5, 5, 0.5, 0.8,0.22, 1.5, 2.6, 0.25,0.14, 0.22, 0.13, 0.18, 0.27, 0.5)


# In[4]:


#Display the right data (Volt Rate Values)

print('HeartRate is: {}'.format(ecg_right.HeartRate))
print('AtrialAmplitude is: {}'.format(ecg_right.AtrialAmplitude))
print('VenAmplitude is: {}'.format(ecg_right.VenAmplitude))
print('AtrialPulseWidth is: {}'.format(ecg_right.AtrialPulseWidth))
print('VentricularPulseWidth is: {}'.format(ecg_right.VentricularPulseWidth))
print('P_waves is: {}'.format(ecg_right.P_waves))
print('QRS_waves is: {}'.format(ecg_right.QRS_waves))
print('ST_up is: {}'.format(ecg_right.ST_up))
print('T_wave is: {}'.format(ecg_right.T_wave))


# In[5]:


#Display the right data (Time Values)

print('P_time is: {}'.format(ecg_right.P_time))
print('PR_time is: {}'.format(ecg_right.PR_time))
print('QRS_time is: {}'.format(ecg_right.QRS_time))
print('ST_time is: {}'.format(ecg_right.ST_time))
print('T_time is: {}'.format(ecg_right.T_time))
print('QT_time is: {}'.format(ecg_right.QT_time))


# # Wrong ECG

# In[6]:


#Calculate the frequency for the wrong data to use it to draw the ECG wave

frequency_wrong = ecg_wrong.HeartRate / ecg_wrong.QRS_time

frequency_wrong


# In[7]:


import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
import numpy as np
  
ecg = electrocardiogram()
  
time_data = np.arange(ecg.size) / frequency_wrong
  
plt.plot(time_data, ecg, color = 'r')
plt.xlabel("time in seconds"  , color = 'b')
plt.ylabel("ECG in milli Volts", color = 'b')
plt.xlim(9, 10.2 )
plt.ylim(-1.5, 2.5 )
plt.title('ECG before using Pacemaker', color = 'b')
plt.savefig("ecg_wrong.png")
plt.show()


# # Right ECG

# In[8]:


#Calculate the frequency for the right data to use it to draw the ECG wave

frequency_right = ecg_right.HeartRate / ecg_right.QRS_time

frequency_right


# In[9]:


import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
import numpy as np
  
ecg = electrocardiogram()
  
time_data = np.arange(ecg.size) / frequency_right
  
plt.plot(time_data, ecg)
plt.xlabel("time in seconds")
plt.ylabel("ECG in milli Volts")
plt.xlim(9, 10.2)
plt.ylim(-1.5, 2.5)
plt.title('ECG after using Pacemaker')
plt.savefig("ecg_right.png")
plt.show()


# In[ ]:




