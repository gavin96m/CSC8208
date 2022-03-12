class IO:

        def __init__(self, LowerRateLimit, UpperRateLimit, FixedAVDelay, DynamicAVDelay, SensedAVDelayOffset,
                     AtrialAmplitude, VentricualrAmplitude, AtrialPulseWidth, VentricularPulseWidth, AtrialSensitivity,
                     VentricularSensitivity, VRP, ARP, Hysteresis, PVARP, PVARPExtension, RateSmoothing, ATRDuration, ATRFallbackMode,
                     ATRFallbackTime):

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

        def heart_values(self):

            param = [self.LowerRateLimit, self.UpperRateLimit, self.FixedAVDelay, self.DynamicAVDelay,
                     self.SensedAVDelayOffset, self.AtrialAmplitude
                , self.VentricualrAmplitude, self.AtrialPulseWidth, self.VentricularPulseWidth, self.AtrialSensitivity,
                     self.VentricularSensitivity
                , self.VRP, self.ARP, self.Hysteresis, self.PVARP, self.PVARPExtension, self.RateSmoothing,
                     self.ATRDuration, self.ATRFallbackMode, self.ATRFallbackTime]

            for par in param:
                if par == None:
                    print('None')
                else:
                    print(par)

def Main():
    ecg_info=IO(60, 90, 150, "OFF", "OFF", 5, 5, 0.5, 0.8, 2, 0.9, 350, 400, "OFF", 350, "OFF", "OFF", "OFF", 20, 1)
    IO.heart_values(ecg_info)


if __name__  == '__main__':
    Main()