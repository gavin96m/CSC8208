# @Time    : 2022-03-11 6:48 p.m.
# @Author  : Xiaoxia Li
# @FileName: lead.py
# @Software: PyCharm
from time import sleep

from pacemaker.heart import Heart
from pacemaker.heart_controller import HeartController

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

class Lead:

    # define chamber
    @staticmethod
    def get_chamber(heart:Heart,chamber):
        if chamber == A:
            return heart.atrial
        if chamber == V:
            return heart.ventricular

# Seperate method
    # define lead
    @staticmethod
    def add_lead_a(type):
        return lead_A

    @staticmethod
    def add_lead_v(type):
        return lead_V

    @staticmethod
    def add_lead_d(type):
        return lead_A, lead_V

    # 1. transit initial heart info from ECG to controller
    @staticmethod
    def transit_heart_info_P():
        initial_p = Heart.heart_arr()[0]
        initial_rr = Heart.heart_arr()[3]
        p_info=[initial_p, initial_rr]
        # send p waveX
        sleep(initial_rr)
        return initial_p

    @staticmethod
    def transit_heart_info_r():
        initial_r = Heart.heart_arr()[1]
        initial_rr = Heart.heart_arr()[3]
        r_info=[initial_r,initial_rr]
        # send r waveX
        sleep(initial_rr)
        return r_info

     # sensitivity, escape interval(after q, before p )
    # 2. Receive information from header
    # It can be expressed in terms of amplitude (volts, milliamps)
    # and pulse width (milliseconds), or energy (microjoules)
    # 起搏脉冲的波形是一个顶部略有下降的方波（如图2．11）。其幅度是指脉冲电压的最大值，一般取5V；其宽度是指脉冲的持续时间，多在0．5～1ms
    def get_generator_info(self):
        header_info = HeartController.transit_pulse()
        return header_info


    # 3. Position 1 Chamber(s) Paced Standard Four-Letter Pacemaker Code\
    # pacing_therapy
    # cardiac depolarization
    def add_pace(self, chamber):
        if chamber == "A":
            return HeartController.pace_atrium()
        elif chamber == "V":
            return HeartController.pace_ventricle()
        elif chamber == "D":
            return HeartController.pace_atrium(), HeartController.pace_ventricle()

    # 4. Position 2 Chamber(s) Sensed
    # II chamber Sensed AVDO
    # input heart beat  output hear beat
    def add_sense(self, chamber):
        if chamber == "A":
            return HeartController.sense_atrium()
        elif chamber == "V":
            return HeartController.sense_ventricle()
        elif chamber == "D":
            return HeartController.sense_atrium(), HeartController.sense_ventricle()

    #5. Position 3 Response to Sensing
    # ITDO
    def add_response(self, mode):
        if mode == "I":
            return HeartController.response_trigger()
        elif mode == "T":
            return HeartController.response_inhibit()
        elif mode == "D":
            return HeartController.response_trigger(), HeartController.response_inhibit()
        else:
            return "None"

    # 6. stimulate
    # occurs T peak to before next q, stimulate V myocardial
    # stronger than normal stimulus can activate the V
    # threshold ia a minimum amount of energy required to rach threshold and evoke an action potential:volts
    # defined by  pulse(amplitude<1.5, duration=0.5)
    # resistant = 400~1200 Ohms
    # I=V/R

    def stimulate(self, pulse_info, resistance, battery ):
        curr_stimulus=pulse_info/resistance
        if curr_stimulus > battery:
            print("ready to stimulate")
            return True

    #7.Modify information from heart/ECG
    def trainsit_output_heart(self):
        # initial_heart_info = Heart.heart_output()
        # return
         pass

