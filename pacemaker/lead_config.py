# @Time    : 2022-03-11 6:48 p.m.
# @Author  : Xiaoxia Li
# @FileName: lead_config.py
# @Software: PyCharm
from time import sleep

from pacemaker.battery import Battery
from pacemaker.heart import Heart
from pacemaker.heart_config import HeartConfig
from pacemaker.lead_object import Lead

lead_A = "AtrialLead"
lead_V = "Ventricular"
A = "Atrial"
V = "Ventricular"
D = "Both"
O = "None"
I = "Inhibit"
T = "T"
pace_A = False
pace_V = False
sense_A = False
sense_V = False

class LeadController:

# Seperate method
    # define lead a
    @staticmethod
    def add_lead_a():
        return lead_A

    # define lead v
    @staticmethod
    def add_lead_v():
        return lead_V

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
    # 起搏脉冲的波形是一个顶部略有下降的方波（如图2．11）。其幅度是指脉冲电压的最大值，一般取5V；其宽度是指脉冲的持续时间，多在0．5～1ms
    def get_pulse_a(self):
        # TODO
        return ["amplitude", "width"]

    def get_generator_info_v(self):
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
        curr_stimulus = amplitude/Lead.resistance
        #TODO
        if curr_stimulus > Battery.consume():
            return "ready to stimulate!!!"

    #3. stimulate a
    def stimulate_v(self):
        # pulse_info, resistance, battery
        self.add_lead_v()
        amplitude = self.get_pulse_v()[0]
        width = self.get_pulse_v()[1]
        curr_stimulus = amplitude/Lead.resistance
        #TODO
        if curr_stimulus > Battery.consume():
            return "ready to stimulate!!!"
