#!/usr/bin/env python
# coding: utf-8

# In[5]:


class InputData:
    
    
    def __init__(self, lower_rate_limit , upper_rate_limit, fixed_AV_delay , dynamic_AV_delay , sensed_AV_delay_offset,atrial_amplitude
                ,ventricular_amplitude, atrial_pulse_width, ventricular_pulse_width, atrial_sensitivity, ventricular_sensitivity
                ,VRP, ARP, hysteresis, PVARP, PVARP_extension,
                 rate_smoothing, ATR_duration, ATR_fallback_mode,ATR_fallback_time):
        
        self.lower_rate_limit = lower_rate_limit
        self.upper_rate_limit = upper_rate_limit
        self.fixed_AV_delay = fixed_AV_delay
        self.dynamic_AV_delay = dynamic_AV_delay
        self.sensed_AV_delay_offset = sensed_AV_delay_offset
        self.atrial_amplitude = atrial_amplitude
        self.ventricular_amplitude = ventricular_amplitude
        self.atrial_pulse_width = atrial_pulse_width
        self.ventricular_pulse_width = ventricular_pulse_width
        self.atrial_sensitivity = atrial_sensitivity
        self.ventricular_sensitivity = ventricular_sensitivity
        self.VRP = VRP
        self.ARP = ARP
        self.hysteresis = hysteresis
        self.PVARP = PVARP
        self.PVARP_extension = PVARP_extension
        self.rate_smoothing = rate_smoothing
        self.ATR_duration = ATR_duration
        self.ATR_fallback_mode = ATR_fallback_mode
        self.ATR_fallback_time = ATR_fallback_time
        
    def check_values(self):
    
        
        param = [self.lower_rate_limit , self.upper_rate_limit, self.fixed_AV_delay , self.dynamic_AV_delay , self.sensed_AV_delay_offset,self.atrial_amplitude
                ,self.ventricular_amplitude, self.atrial_pulse_width, self.ventricular_pulse_width, self.atrial_sensitivity, self.ventricular_sensitivity
                ,self.VRP, self.ARP, self.hysteresis, self.PVARP, self.PVARP_extension, self.rate_smoothing, self.ATR_duration, self.ATR_fallback_mode,self.ATR_fallback_time]

        # int
        # lower_rate_limit,upper_rate_limit,,fixed_AV_delay,,
        ## maximum_sensor,minimum_dynamic_AV_delay

        # bool
        # dynamic_AV_delay,

        # "OFF" or int
        # sensed_AV_delay_offset,

        # "OFF" or float



        for par in param:
            if par == "OFF":
                print('OFF')
            else:
                # par = int()
                print(par)

if __name__ == '__main__':
    # "60","120","150","OFF","OFF","3.5",
    # "3.5","0.4","0.4","0.75","2.5",
    # "320","250","OFF","250","OFF",
    # "OFF","OFF","20","1"

    # io = IO("60","120","150","OFF","OFF","3.5",
    #         "3.5","0.4","0.4","0.75","2.5",
    #         "320","250","OFF","250","OFF",
    #         "OFF","OFF","20","1")
    io2 = InputData(60,120,150,"OFF","OFF",3.5,3.5,0.4,0.4,0.75,2.5,320,250,"OFF",250,"OFF","OFF","OFF",20,1)

    io2.check_values()