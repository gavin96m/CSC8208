#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ECG:
    # Constructor
    def __init__(self, P_waves, QRS_waves, ST_up, T_wave,
                 P_time, PR_time, QRS_time, ST_time, T_time, QT_time):
       
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

ecg_right = ECG(4 ,6 , 1.6, 0.6,0.12, 0.13, 0.08, 0.09, 0.1, 0.43)


# # Right ECG

# In[3]:


duration_time = [0.06 , 0.12 , 0.08 , 0.15 , 0.11 , 0.10]

dist1 = duration_time[1] - duration_time[0] 
dist2 = duration_time[2] - duration_time[1] 
dist3 = duration_time[3] - duration_time[2] 
dist4 = duration_time[4] - duration_time[3] 
dist5 = duration_time[5] - duration_time[4] 


# In[4]:


avg = (dist1 + dist2 + dist3 + dist4 + dist5) / 5
avg = avg * 1000


# In[5]:


Heart_Rate = avg * 10


# In[6]:


frequency = Heart_Rate / ecg_right.T_time

frequency


# In[7]:


import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
import numpy as np
  
ecg = electrocardiogram()
  
time_data = np.arange(ecg.size) / frequency
  
plt.plot(time_data, ecg)
plt.xlabel("time in seconds")
plt.ylabel("ECG in milli Volts")
plt.xlim(9, 10.2)
plt.ylim(-1.5, 3)
plt.title('ECG after using Pacemaker')
plt.show()

print(int(Heart_Rate))

if Heart_Rate > 60 and Heart_Rate < 120:
    print('Regular')
    
else:
    print('Irregular')


# # Wrong ECG

# In[8]:


#take an object from ECG class with the wrong data

ecg_wrong = ECG(4 , 1.5, 2.6, 0.25,0.14, 0.22, 0.13, 0.18, 0.27, 0.5)


# In[9]:


duration_time = [0.09 , 0.32 , 0.18 , 0.42 , 0.1 , 0.11]

dist1 = duration_time[1] - duration_time[0] 
dist2 = duration_time[2] - duration_time[1] 
dist3 = duration_time[3] - duration_time[2] 
dist4 = duration_time[4] - duration_time[3] 
dist5 = duration_time[5] - duration_time[4] 


# In[10]:


avg = (dist1 + dist2 + dist3 + dist4 + dist5) / 5
avg = avg * 1000


# In[11]:


Heart_Rate = avg * 10


# In[12]:


#Calculate the frequency for the wrong data to use it to draw the ECG wave

frequency_wrong = Heart_Rate / ecg_wrong.T_time

frequency_wrong


# In[13]:


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
plt.show()


print(int(Heart_Rate))

if Heart_Rate > 60 and Heart_Rate < 120:
    print('Regular')
    
else:
    print('Irregular')


# In[ ]:





# In[14]:


#Display the right data (Volt Rate Values)

print('P_waves is: {}'.format(ecg_right.P_waves))
print('QRS_waves is: {}'.format(ecg_right.QRS_waves))
print('ST_up is: {}'.format(ecg_right.ST_up))
print('T_wave is: {}'.format(ecg_right.T_wave))


# In[15]:


#Display the right data (Time Values)

print('P_time is: {}'.format(ecg_right.P_time))
print('PR_time is: {}'.format(ecg_right.PR_time))
print('QRS_time is: {}'.format(ecg_right.QRS_time))
print('ST_time is: {}'.format(ecg_right.ST_time))
print('T_time is: {}'.format(ecg_right.T_time))
print('QT_time is: {}'.format(ecg_right.QT_time))


# In[ ]:




