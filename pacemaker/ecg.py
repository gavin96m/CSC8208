# class ECG:
#     # Constructor
#     def __init__(self, P_waves, QRS_waves, ST_up, T_wave,
#                  P_time, PR_time, QRS_time, ST_time, T_time, QT_time):
#
#         self.P_waves = P_waves
#         self.QRS_waves = QRS_waves
#         self.ST_up = ST_up
#         self.T_wave = T_wave
#         self.P_time = P_time
#         self.PR_time = PR_time
#         self.QRS_time = QRS_time
#         self.ST_time = ST_time
#         self.T_time = T_time
#         self.QT_time = QT_time
#
# # In[2]:
# # take an object from ECG class with the right data
# ecg_right = ECG(0.22, 1.5, 2.6, 0.25, 0.14, 0.22, 0.13, 0.18, 0.27, 0.5)
#
# # In[3]:
# ecg_wrong = ECG ( 0.12, 1.0, 1.6, 0.6, 0.12, 0.13, 0.08, 0.09, 0.2, 0.43)
#
# # In[4]:
# # Calculate the frequency for the wrong data to use it to draw the ECG wave
# frequency_wrong = 60 / ecg_wrong.QRS_time
# frequency_wrong
#
# # In[7]:
#
#
# import matplotlib.pyplot as plt
# # from scipy.misc import electrocardiogram
# import numpy as np
#
# ecg = electrocardiogram()
#
# time_data = np.arange(ecg.size) / frequency_wrong
#
# plt.plot(time_data, ecg, color='r')
# plt.xlabel("time in seconds", color='b')
# plt.ylabel("ECG in milli Volts", color='b')
# plt.xlim(9, 10.2)
# plt.ylim(-1.5, 2.5)
# plt.title('ECG before using Pacemaker', color='b')
# plt.savefig("ecg_wrong.png")
# plt.show()
#
# # # Right ECG
#
# # In[8]:
# # Calculate the frequency for the right data to use it to draw the ECG wave
# frequency_right = 60/ ecg_right.QRS_time+ecg_right.T_time
#
# frequency_right
# # In[9]:
#
# ecg = electrocardiogram()
# time_data = np.arange(ecg.size) / frequency_right
# plt.plot(time_data, ecg)
# plt.xlabel("time in seconds")
# plt.ylabel("ECG in milli Volts")
# plt.xlim(9, 10.2)
# plt.ylim(-1.5, 2.5)
# plt.title('ECG after using Pacemaker')
# plt.savefig("ecg_right.png")
# plt.show()