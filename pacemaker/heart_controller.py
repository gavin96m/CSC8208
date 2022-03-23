import _thread
from time import sleep
import io
from lead import LeadController

class PacemakerBasic:
    def __init__(self,pacemaker_obj):
        self.lower_rate_limit = pacemaker_obj["lower_rate_limit"]
        self.upper_rate_limit = pacemaker_obj["upper_rate_limit"]
        self.fixed_AV_delay = pacemaker_obj["fixed_AV_delay"]
        self.dynamic_AV_delay = pacemaker_obj["dynamic_AV_delay"]
        self.sensed_AV_delay_offset = pacemaker_obj["sensed_AV_delay_offset"]
        self.atrial_amplitude = pacemaker_obj["atrial_amplitude"]
        self.ventricular_amplitude = pacemaker_obj["ventricular_amplitude"]
        self.atrial_pulse_width = pacemaker_obj["atrial_pulse_width"]
        self.ventricular_pulse_width = pacemaker_obj["ventricular_pulse_width"]
        self.atrial_sensitivity = pacemaker_obj["atrial_sensitivity"]
        self.ventricular_sensitivity = pacemaker_obj["ventricular_sensitivity"]
        self.VRP = pacemaker_obj["VRP"]
        self.ARP = pacemaker_obj["ARP"]
        self.hysteresis = pacemaker_obj["hysteresis"]
        self.PVARP = pacemaker_obj["PVARP"]
        self.PVARP_extension = pacemaker_obj["PVARP_extension"]
        self.rate_smoothing = pacemaker_obj["rate_smoothing"]
        self.ATR_duration = pacemaker_obj["ATR_duration"]
        self.ATR_fallback_mode = pacemaker_obj["ATR_fallback_mode"]
        self.ATR_fallback_time = pacemaker_obj["ATR_fallback_time"]
        self.a_blacking_period = pacemaker_obj["a_blacking_period"]
        self.v_blacking_period = pacemaker_obj["v_blacking_period"]


    # heart_rate,
    # RR_interval = 60000/heart_rate
    # def get_heart_info():
    #     heart_rate = transit_heart_info()
    def pace_atrium(self,lower_rate_limit):
        # 防止心跳过慢，当到点了 还没感知到时，激活
        interval = self.calc_interval(lower_rate_limit)
        return interval

    def pace_ventricular(self,lower_rate_limit):
        interval = self.calc_interval(lower_rate_limit)
        return interval



    # each time finished means end this interval
    def sense_atrium(self,pacemaker_obj,interval,time, p_wave, sense_type):
        has_sense = False
        between_ARP = False

        # not sensed
        if p_wave < pacemaker_obj.atrial_sensitivity:
            interval = interval-pacemaker_obj.atrial_pulse_width
            if sense_type == "trigger":
                # sleep(max(interval,pacemaker_obj.ARP)/1000)
                # sleep(pacemaker_obj.ARP/1000)
                # sleep(interval/1000)
                print("trigger",interval/1000)
            else:
                sleep(max(pacemaker_obj.ARP,pacemaker_obj.PVARP)/1000)
                # print("inhibit",pacemaker_obj.ARP)

        # normal
        # continue sense
        else:
            # if between ARP
            if time<=pacemaker_obj.ARP:
                # Noise
                between_ARP = True
                has_sense = True
            # sense
            # break & reset time
            else:
            #     time after ARP
                print("reset")
                has_sense = True
        return has_sense,between_ARP

    def sense_ventricular(self,pacemaker_obj, interval, r_wave, sense_type):
        has_sense = False
        # too slow / not sensed
        if r_wave < pacemaker_obj.ventricular_sensitivity:
            interval = interval-pacemaker_obj.ventricular_pulse_width
            if sense_type == "trigger":
                sleep(max(pacemaker_obj.VRP,pacemaker_obj.PVARP)/1000)
                print("trigger",(max(pacemaker_obj.VRP,pacemaker_obj.PVARP)))
            # inhibit
            else:
                sleep(pacemaker_obj.VRP/1000)
                print("inhibit")
        # inhibit
        # normal
        # continue sense
        else:
            print("normal")
            has_sense = True
        return has_sense

    @staticmethod
    def trigger(lead,pulse_info):
        # print(amplitude,pulse_width)
        sleep(pulse_info[1]/1000)
        lead.stimulate_a(pulse_info)
        return pulse_info

    # hystersis is OFF
    def inhibit(self,lead):

        pass


    # def set_mode():
    #     pass
    #
    # def set_interval():
    #     pass
    #
    # def add_lead_pacer():
    #     pass

    @staticmethod
    def calc_interval(rate_limit):

        interval = 60000 / rate_limit
        return interval

    @staticmethod
    def calc_heart_rate(interval):
        heart_rate = 60000 / interval
        return heart_rate


class HeartController:

    def AOO(self, pacemaker_obj, lead: LeadController):
        # pacemaker.lower_rate_limit,
        # pacemaker.upper_rate_limit,
        # pacemaker.atrial_amplitude,
        # pacemaker.atrial_pulse_width,
        interval = pacemaker_obj.pace_atrium(pacemaker_obj.lower_rate_limit) - pacemaker_obj.atrial_pulse_width
        sleep(interval / 1000)
        print(pacemaker_obj.atrial_amplitude, pacemaker_obj.atrial_pulse_width)
        pulse_info = [pacemaker_obj.atrial_amplitude, pacemaker_obj.atrial_pulse_width]
        lead.stimulate_a(pulse_info)

    def VOO(self, pacemaker_obj, lead: LeadController):
        # pacemaker.lower_rate_limit,
        # pacemaker.upper_rate_limit,
        # pacemaker.ventricular_amplitude,
        # pacemaker.ventricular_pulse_width
        interval = pacemaker_obj.pace_ventritular(
            pacemaker_obj.lower_rate_limit) - pacemaker_obj.ventritular_pulse_width
        sleep(interval / 1000)
        print(pacemaker_obj.ventritular_amplitude, pacemaker_obj.ventritular_pulse_width)
        pulse_info = [pacemaker_obj.ventritular_amplitude, pacemaker_obj.ventritular_pulse_width]
        lead.stimulate_a(pulse_info)

    def AAT(self, pacemaker_obj:PacemakerBasic, lead_a, p_wave, elapsed_time):

        if elapsed_time/1000 < pacemaker_obj.ARP:
            # between ARP
            return 0
        else:
            # no sense
            if p_wave < pacemaker_obj.atrial_sensitivity:
                pulse_info = [pacemaker_obj.atrial_amplitude,pacemaker_obj.atrial_pulse_width]
                pacemaker_obj.trigger(lead_a,pulse_info)
                return 2
            else:
                return 1

    def VVT(self, pacemaker_obj:PacemakerBasic, lead_v, r_wave, elapsed_time):

        if elapsed_time / 1000 < pacemaker_obj.VRP:
            # between ARP
            return 0
        else:
            # no sense
            if r_wave < pacemaker_obj.ventricular_sensitivity:
                pulse_info = [pacemaker_obj.ventricular_amplitude, pacemaker_obj.ventricular_pulse_width]
                pacemaker_obj.trigger(lead_v, pulse_info)
                return 2
            else:
                return 1

    def AAI(self, pacemaker_obj:PacemakerBasic, lead_a, p_wave, elapsed_time):

        if elapsed_time / 1000 < pacemaker_obj.ARP:
            # between ARP
            return 0

        else:
            if p_wave > pacemaker_obj.atrial_sensitivity:
                pacemaker_obj.inhibit(lead_a)
                return 1

            pulse_info = [pacemaker_obj.atrial_amplitude, pacemaker_obj.atrial_pulse_width]
            pacemaker_obj.trigger(lead_a, pulse_info)
            return 2

    def VVI(self, pacemaker_obj:PacemakerBasic, lead_v, r_wave, elapsed_time):

        if elapsed_time / 1000 < pacemaker_obj.VRP:
            # between VRP
            return 0

        else:
            if r_wave > pacemaker_obj.ventricular_sensitivity:
                pacemaker_obj.inhibit(lead_v)
                return 1

            pulse_info = [pacemaker_obj.ventricular_amplitude, pacemaker_obj.ventricular_pulse_width]
            pacemaker_obj.trigger(lead_v, pulse_info)
            return 2

    def DDD(self, pacemaker):
