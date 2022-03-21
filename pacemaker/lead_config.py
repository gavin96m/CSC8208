# @Time    : 2022-03-11 18:22 p.m.
# @Author  : Xiaoxia Li
# @FileName: lead.py
# @Software: PyCharm
# Description: a basic class for lead object
class Lead(object):

    def __init__(self, atrial_lead, ventricular_lead, resistance):
        self.resistance = resistance
        self.atrial_lead = atrial_lead
        self.ventricular_lead = ventricular_lead

    def lead_a(self):
        return self.atrial_lead

    def lead_v(self):
        return self.ventricular_lead

    def resistance(self):
        self.resistance=100
        return self.resistance

    # toString
    def __str__(self):
        return "%s: %s %s" % (self.atrial_lead, self.ventricular_lead, self.resistance)  #


def main():
    # Lead.atrial_lead = "Atrial"
    # Lead.ventricular_lead = "Ventricular"
    # s2 = [Lead.resistance1, Lead.atrial_lead, Lead.ventricular_lead]
    # print(s2)

    if __name__ == '__main__':
        main()


from pacemaker.battery import Battery
from pacemaker.heart_config import HeartConfig


class LeadController:
    # define lead a
    @staticmethod
    def add_lead_a():
        return Lead.lead_a()

    # define lead v
    @staticmethod
    def add_lead_v():
        return Lead.lead_v()

    # 1. transit initial heart info from ECG to controller
    @staticmethod
    def transit_heart_info_p():
        return HeartConfig.transit_p()

    @staticmethod
    def transit_heart_info_r():
        return HeartConfig.transit_qrs()

    @staticmethod
    def transit_heart_info_pp():
        return HeartConfig.cal_pp()

    @staticmethod
    def transit_heart_info_rr():
        return HeartConfig.cal_rr()

    # 2. Receive information from header
    # It can be expressed in terms of amplitude (volts, milliamps)
    # and pulse width (milliseconds), or energy (microjoules)
    @staticmethod
    def get_pulse_a():
        # TODO
        return ["amplitude", "width"]

    @staticmethod
    def get_generator_info_v():
        return ["amplitude", "width"]

    # 3. stimulate a
    # occurs T peak to before next q, stimulate V myocardial
    # stronger than normal stimulus can activate the V
    # threshold ia a minimum amount of energy required to rach threshold and evoke an action potential:volts
    # defined by  pulse(amplitude<1.5, duration=0.5)
    # resistant = 400~1200 Ohms
    # I=V/R
    def stimulate_a(self):
        # pulse_info, resistance, battery
        self.add_lead_a()
        amplitude = self.get_pulse_a()[0]
        width = self.get_pulse_a()[1]
        curr_stimulus = amplitude/100
        #TODO
        if curr_stimulus > Battery.consume():
            return "ready to stimulate!!!"

    # 3. stimulate a
    def stimulate_v(self):
        # pulse_info, resistance, battery
        self.add_lead_v()
        amplitude = self.get_pulse_v()[0]
        width = self.get_pulse_v()[1]
        curr_stimulus = amplitude/Lead.resistance
        #TODO
        if curr_stimulus > Battery.consume():
            return "ready to stimulate!!!"

