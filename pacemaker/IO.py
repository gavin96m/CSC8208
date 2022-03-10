#!/usr/bin/env python
# coding: utf-8

# In[5]:


class IO:
    
    
    def __init__(self, LowerRateLimit , UpperRateLimit, FixedAVDelay , DynamicAVDelay , SensedAVDelayOffset,AtrialAmplitude
                ,VentricualrAmplitude, AtrialPulseWidth, VentricularPulseWidth, AtrialSensitivity, VentricularSensitivity
                ,VRP, ARP, Hysteresis, PVARP, PVARPExtension, RateSmoothing, ATRDuration, ATRFallbackMode,ATRFallbackTime):
        
        self.LowerRateLimit = LowerRateLimit
        self.UpperRateLimit = UpperRateLimit
        self.FixedAVDelay = FixedAVDelay
        self.DynamicAVDelay = DynamicAVDelay
        self.SensedAVDelayOffset = SensedAVDelayOffset
        self.AtrialAmplitude = AtrialAmplitude
        self.VentricualrAmplitude = VentricualrAmplitude
        self.AtrialPulseWidth = AtrialPulseWidth
        self.VentricularPulseWidth = VentricularPulseWidth
        self.AtrialSensitivity = AtrialSensitivity
        self.VentricularSensitivity = VentricularSensitivity
        self.VRP = VRP
        self.ARP = ARP
        self.Hysteresis = Hysteresis
        self.PVARP = PVARP
        self.PVARPExtension = PVARPExtension
        self.RateSmoothing = RateSmoothing
        self.ATRDuration = ATRDuration
        self.ATRFallbackMode = ATRFallbackMode
        self.ATRFallbackTime = ATRFallbackTime
        
    def check_values(self):
    
        
        param = [self.LowerRateLimit , self.UpperRateLimit, self.FixedAVDelay , self.DynamicAVDelay , self.SensedAVDelayOffset,self.AtrialAmplitude
                ,self.VentricualrAmplitude, self.AtrialPulseWidth, self.VentricularPulseWidth, self.AtrialSensitivity, self.VentricularSensitivity
                ,self.VRP, self.ARP, self.Hysteresis, self.PVARP, self.PVARPExtension, self.RateSmoothing, self.ATRDuration, self.ATRFallbackMode,self.ATRFallbackTime]
        
        for par in param:
            if par == None:
                print('None')
            else:
                print(int(par))
  


# In[9]:


io = IO(None , '2' , 0.03 , '4' ,None , 6 , '7' , None , 9 , 10 , None ,  12 , 14 , 15 , None , 17 , 18 ,19 ,None , 21)


# In[10]:


io.ATRDuration


# In[11]:


io.check_values()


# In[ ]:




