# @Time    : 2022-03-11 18:22 p.m.
# @Author  : Xiaoxia Li
# @FileName: lead.py
# @Software: PyCharm
# Description: a basic class for lead object


# from pacemaker.battery import Battery
from heart import HeartConfig as heart_config


class Lead(object):

    def __init__(self, atrial_lead, ventricular_lead, resistance):
        self.resistance = resistance
        self.atrial_lead = atrial_lead
        self.ventricular_lead = ventricular_lead


    @staticmethod
    def lead_a():
        return "atrial_lead"

    @staticmethod
    def lead_v():
        return "ventricular_lead"

    @staticmethod
    def resistance():
        return 400

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


class LeadController:
    # define lead a
    @staticmethod
    def add_lead_a():
        return Lead.lead_a()

    # define lead v
    @staticmethod
    def add_lead_v():
        return Lead.lead_v()

    @staticmethod
    def get_chamber_a():
        return heart_config.transit_chamber_a()

    # define chamber ventricular
    @staticmethod
    def get_chamber_v():
        return heart_config.transit_chamber_v()

    @staticmethod
    def get_chamber_d():
        return heart_config.transit_chamber_d()

    # 1. transit initial heart info from ECG to controller
    @staticmethod
    def transit_heart_info_p(heart_config, i):
        return heart_config.transit_p(heart_config, i)

    @staticmethod
    def transit_heart_info_r(heart_config, i):
        return heart_config.transit_qrs(heart_config, i)

    @staticmethod
    def transit_heart_info_pp(heart_config, i):
        return heart_config.cal_pp(heart_config, i)

    @staticmethod
    def transit_heart_info_rr(heart_config, i):
        return heart_config.cal_rr(heart_config, i)

    # 2. Receive information from header
    # It can be expressed in terms of amplitude (volts, milliamps)
    # and pulse width (milliseconds), or energy (microjoules)
    @staticmethod
    def get_pulse_a(pulse_info):
        return pulse_info

    @staticmethod
    def get_pulse_v(pulse_info):
        return pulse_info

    # 3. ready to stimulate, calculate
    # resistant = 400~1200 Ohms
    # I=V/R
    def prepare_stimulate_a(self, pulse_info):
        # pulse_info, resistance, battery
        amplitude = pulse_info[0]
        width = pulse_info[1]
        curr_stimulus = amplitude / Lead.resistance()
        return pulse_info, curr_stimulus

    # 3. stimulate a
    def prepare_stimulate_v(self, pulse_info):
        # pulse_info, resistance, battery
        amplitude = pulse_info[0]
        width = pulse_info[1]
        curr_stimulus = amplitude / Lead.resistance()
        return pulse_info, curr_stimulus

    def stimulate_a(self, pulse_info):
        pulse_info = self.get_pulse_a(pulse_info)
        stimulate_info = self.prepare_stimulate_a(self, pulse_info)
        return "Stimulating Heart in: " + self.get_chamber_a() + ", with lead: " + self.add_lead_a() \
               + ", pulse amplitude and width are: " + str(stimulate_info)

    def stimulate_v(self, pulse_info):
        pulse_info = self.get_pulse_v(pulse_info)
        stimulate_info = self.prepare_stimulate_v(self, pulse_info)
        return "Stimulating Heart in: " + self.get_chamber_v() + ", with lead: " + self.add_lead_v() \
               + ", pulse amplitude and width are: " + str(stimulate_info)

    def get_chamber(self, chamber):
        if chamber == "Atrial":
            return self.get_chamber_a()
        if chamber == "Ventricular":
            return self.get_chamber_v()
        if chamber == "Both":
            return self.get_chamber_d()




def main():
    print(LeadController.transit_heart_info_p(heart_config, 0))
    print(LeadController.transit_heart_info_r(heart_config, 0))
    print(LeadController.transit_heart_info_rr(heart_config, 0))
    print(LeadController.stimulate_v(LeadController, [3.5, 0.4]))
    print(LeadController.stimulate_a(LeadController, [3.5, 0.4]))


if __name__ == '__main__':
    main()