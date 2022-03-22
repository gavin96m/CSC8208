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

    def trigger(self,amplitude,pulse_width):
        print(amplitude,pulse_width)
        sleep(pulse_width/1000)
        # TODO: send to lead
        return amplitude,pulse_width

    # hystersis is OFF
    def inhibit(self,pulse_width):

        print(pulse_width)
        sleep(pulse_width/1000)
        # TODO: send NONE to lead

    # hysteresis is not OFF
    def inhibit(self,pulse_width,hysteresis,hate_rate):
        # lower than LRL, larger than hysteresis
        # 抑制


        return None

        # higher than both
        # 抑制

        # lower than both
        # 不抑制


        print(pulse_width)



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
    
class PacemakerController():
    def AAT(self, pacemaker_obj, lead, elapsed_time=0):
        # pacemaker_obj.lower_rate_limit
        # pacemaker_obj.upper_rate_limit
        # pacemaker_obj.atrial_amplitude
        # pacemaker_obj.atrial_pulse_width
        # pacemaker_obj.atrial_sensitivity,
        # pacemaker_obj.ARP,
        # pacemaker_obj.PVARP
        # rest of time
        interval = pacemaker_obj.pace_atrium(pacemaker_obj.lower_rate_limit) - elapsed_time
        # todo get P_wave
        p_wave = lead.transit_heart_info_p()

        has_sense, between_ARP = pacemaker_obj.sense_atrium(pacemaker_obj, interval, p_wave, "trigger")
        if not has_sense:
            pacemaker_obj.trigger(pacemaker_obj.atrial_amplitude, pacemaker_obj.atrial_pulse_width)
            sleep((interval - pacemaker_obj.atrial_pulse_width - pacemaker_obj.ARP) / 1000)
        # has_sense
        elif has_sense:
            sleep(interval / 1000)
        # noise
        else:
            pass

        # return pacemaker_obj.atrial_amplitude, pacemaker_obj.atrial_pulse_width, time
    # while True:
    #     # sensed ventricular
    #     if sensed_ventricular:
    #         continue
    #     interval = 60000
    #
    #     pacemaker.ARP
    #
    # interval = 60000 / pacemaker.lower_rate_limit
    #
    # return pacemaker.atrial_amplitude, pacemaker.atrial_pulse_width,pacemaker.atrial_sensitivity

    def VVT(self, pacemaker_obj: io, lead):
        # pacemaker.lower_rate_limit,
        # pacemaker.upper_rate_limit,
        # pacemaker.ventricular_amplitude,
        # pacemaker.ventricular_pulse_width,
        # pacemaker.ventricular_sensitivity,
        # pacemaker.VRP
        interval = pacemaker_obj.pace_ventricular(pacemaker_obj.lower_rate_limit)
        # todo get r_wave
        lead.transit_heart_info_rr()
        r_wave = 110
        has_sense = pacemaker_obj.sense_ventricular(pacemaker_obj, interval, r_wave, "trigger")
        if not has_sense:
            self.trigger(pacemaker_obj.ventricular_amplitude, pacemaker_obj.ventricular_pulse_width)
            sleep((interval - pacemaker_obj.ventricular_pulse_width - pacemaker_obj.ARP) / 1000)
        # has_sense
        else:
            sleep(interval / 1000)
        return pacemaker_obj.ventricular_amplitude, pacemaker_obj.ventricular_pulse_width

    def AOO(self,pacemaker_obj, lead: LeadController):
        # pacemaker.lower_rate_limit,
        # pacemaker.upper_rate_limit,
        # pacemaker.atrial_amplitude,
        # pacemaker.atrial_pulse_width,
        interval = pacemaker_obj.pace_atrium(pacemaker_obj.lower_rate_limit) - pacemaker_obj.atrial_pulse_width
        sleep(interval / 1000)
        print(pacemaker_obj.atrial_amplitude, pacemaker_obj.atrial_pulse_width)
        pulse_info = [pacemaker_obj.atrial_amplitude, pacemaker_obj.atrial_pulse_width]
        lead.stimulate_a(pulse_info)

    def AAI(self, pacemaker_obj):
        #     pacemaker.lower_rate_limit,
        #     pacemaker.upper_rate_limit,
        #     pacemaker.atrial_amplitude,
        #     pacemaker.atrial_pulse_width,
        #     pacemaker.atrial_sensitivity,
        #     pacemaker.ARP,
        #     pacemaker.PVARP,
        #     pacemaker.hysteresis,
        #     pacemaker.rate_smoothing
        interval = pacemaker_obj.pace_atrium(pacemaker_obj.lower_rate_limit)
        # todo get p_wave
        p_wave = 1000
        has_sense = pacemaker_obj.sense_atrium(pacemaker_obj, interval, p_wave, "inhibit")
        if has_sense:
            # no hysteresis
            if not pacemaker_obj.hysteresis:
                #     inhibit(pulse_width):
                pacemaker_obj.inhibit(pacemaker_obj.atrial_pulse_width)
            # hysteresis
            else:
                #            inhibit(pulse_width,hysteresis,hate_rate):
                pacemaker_obj.inhibit(pacemaker_obj.atrial_pulse_width, pacemaker_obj.hysteresis, pacemaker_obj.hate_rate)
        else:
            return pacemaker_obj.pulse_width, pacemaker_obj.hysteresis

    def VOO(self ,pacemaker_obj, lead: LeadController):
        # pacemaker.lower_rate_limit,
        # pacemaker.upper_rate_limit,
        # pacemaker.ventricular_amplitude,
        # pacemaker.ventricular_pulse_width
        interval = pacemaker_obj.pace_ventritular(pacemaker_obj.lower_rate_limit) - pacemaker_obj.ventritular_pulse_width
        sleep(interval / 1000)
        print(pacemaker_obj.ventritular_amplitude, pacemaker_obj.ventritular_pulse_width)
        pulse_info = [pacemaker_obj.ventritular_amplitude, pacemaker_obj.ventritular_pulse_width]
        lead.stimulate_a(pulse_info)

    def VVI(self, pacemaker):
        self.pace_ventricular()
        self.sense_ventricular()
        self.response_inhibit()
        # return [
        #     pacemaker.lower_rate_limit,
        #     pacemaker.upper_rate_limit,
        #     pacemaker.ventricular_amplitude,
        #     pacemaker.ventricular_pulse_width,
        #     pacemaker.ventricular_sensitivity,
        #     pacemaker.VRP,
        #     pacemaker.hysteresis,
        #     pacemaker.rate_smoothing,
        # ]

    def DDI(self, pacemaker):
        self.pace_atrium()
        self.pace_ventricular()
        self.sense_atrium()
        self.sense_ventricular()
        self.response_inhibit()
        # return [
        #     pacemaker.lower_rate_limit,
        #     pacemaker.upper_rate_limit,
        #     pacemaker.fixed_AV_delay,
        #     pacemaker.atrial_amplitude,
        #     pacemaker.ventricular_amplitude,
        #     pacemaker.atrial_pulse_width,
        #     pacemaker.ventricular_pulse_width,
        #     pacemaker.atrial_sensitivity,
        #     pacemaker.ventricular_sensitivity,
        #     pacemaker.VRP,
        #     pacemaker.ARP,
        #     pacemaker.PVARP,
        # ]

    def DDD(self, pacemaker):
        self.pace_ventricular()
        self.pace_ventricular()
        self.sense_atrium()
        self.sense_ventricular()
        self.response_trigger()
        self.response_inhibit()
        # return [
        #     pacemaker.lower_rate_limit,
        #     pacemaker.upper_rate_limit,
        #     pacemaker.fixed_AV_delay,
        #     pacemaker.dynamic_AV_delay,
        #     pacemaker.sensed_av_delay_offset,
        #     pacemaker.atrial_amplitude,
        #     pacemaker.ventricular_amplitude,
        #     pacemaker.atrial_pulse_width,
        #     pacemaker.ventricular_pulse_width,
        #     pacemaker.atrial_sensitivity,
        #     pacemaker.ventricular_sensitivity,
        #     pacemaker.VRP,
        #     pacemaker.ARP,
        #     pacemaker.PVARP,
        #     pacemaker.PVARP_extension,
        #     pacemaker.hysteresis,
        #     pacemaker.rate_smoothing,
        #     pacemaker.atr_duration,
        #     pacemaker.atr_fallback_mode,
        #     pacemaker.atr_fallback_time
        # ]
        # pass