import _thread
from time import sleep
import IO


class HeartController:
    # from parameters import Parameters


    # heart_rate,
    # RR_interval = 60000/heart_rate
    # def get_heart_info():
    #     heart_rate = transit_heart_info()
    #
    # )

    def AAT(self, data: IO):
        # data.lower_rate_limit
        # data.upper_rate_limit
        # data.atrial_amplitude
        # data.atrial_pulse_width
        # data.atrial_sensitivity,
        # data.ARP,
        # data.PVARP
        interval = self.pace_atrium(data.lower_rate_limit)
        # todo get P_wave / heart_rate
        p_wave = True
        to_trigger = self.sense_atrium(data,50,interval,p_wave,"trigger")
        if to_trigger:
            self.trigger(data.atrial_amplitude,data.atrial_pulse_width)
        else:
            sleep(data.atrial_pulse_width/1000)

        return data.atrial_amplitude,data.atrial_pulse_width


    # while True:
    #     # sensed ventricle
    #     if sensed_ventricle:
    #         continue
    #     interval = 60000
    #
    #     pacemaker.ARP
    #
    # interval = 60000 / pacemaker.lower_rate_limit
    #
    # return pacemaker.atrial_amplitude, pacemaker.atrial_pulse_width,pacemaker.atrial_sensitivity

    def VVT(self,data:IO):
            # pacemaker.lower_rate_limit,
            # pacemaker.upper_rate_limit,
            # pacemaker.ventricular_amplitude,
            # pacemaker.ventricular_pulse_width,
            # pacemaker.ventricular_sensitivity,
            # pacemaker.VRP
            interval = self.pace_ventricle(data.lower_rate_limit)
            # todo get r_wave / heart_rate
            r_wave = 1000
            to_trigger = self.sense_ventricle(data, 70, interval, r_wave, "trigger")
            if to_trigger:
                self.trigger(data.ventricular_amplitude,data.ventricular_pulse_width)
            else:
                sleep(data.ventricular_pulse_width/1000)

    def AOO(self,data:IO):
        # pacemaker.lower_rate_limit,
        # pacemaker.upper_rate_limit,
        # pacemaker.atrial_amplitude,
        # pacemaker.atrial_pulse_width,

        interval = self.pace_atrium(data.lower_rate_limit) - data.atrial_pulse_width
        sleep(interval/1000)
        print(data.atrial_amplitude,data.atrial_pulse_width)
        return data.atrial_amplitude,data.atrial_pulse_width


        # return li
        # todo 两个参数（a_amplitude,a_pulse_width)

    def AAI(self,data):
        #     pacemaker.lower_rate_limit,
        #     pacemaker.upper_rate_limit,
        #     pacemaker.atrial_amplitude,
        #     pacemaker.atrial_pulse_width,
        #     pacemaker.atrial_sensitivity,
        #     pacemaker.ARP,
        #     pacemaker.PVARP,
        #     pacemaker.hysteresis,
        #     pacemaker.rate_smoothing
        interval = self.pace_atrium(data.lower_rate_limit)
        # todo get p_wave / heart_rate
        p_wave = 1000
        to_trigger = self.sense_atrium(data, 70, interval, p_wave,"inhibit")
        # 
        if not to_trigger：


    def VOO(self,data:IO):
        # pacemaker.lower_rate_limit,
        # pacemaker.upper_rate_limit,
        # pacemaker.ventricular_amplitude,
        # pacemaker.ventricular_pulse_width
        interval = self.pace_ventricle(data.lower_rate_limit) - data.ventricular_pulse_width
        sleep(interval/1000)
        print(data.ventricular_amplitude,data.ventricular_pulse_width)
        return data.ventricular_amplitude,data.ventricular_pulse_width

    def VVI(self,pacemaker):
        self.pace_ventricle()
        self.sense_ventricle()
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

    def VDD(self,pacemaker):
        self.pace_ventricle()
        self.sense_ventricle()
        self.sense_atrium()
        self.response_trigger()
        self.response_inhibit()
        # return [
        #     pacemaker.lower_rate_limit,
        #     pacemaker.upper_rate_limit,
        #     pacemaker.fixed_AV_delay,
        #     pacemaker.dynamic_AV_delay,
        #     pacemaker.ventricular_amplitude,
        #     pacemaker.ventricular_pulse_width,
        #     pacemaker.VRP,
        #     pacemaker.PVARP_extension,
        #     pacemaker.rate_smoothing,
        #     pacemaker.atr_duration,
        #     pacemaker.atr_fallback_mode,
        #     pacemaker.atr_fallback_time
        # ]
        # pass

    def DOO(self,data):
        try:
            _thread.start_new_thread(self.AOO, (data,))
            _thread.start_new_thread(self.VOO,(data,))
        except Exception as ex:
            print(ex)
        # return [
        #     pacemaker.lower_rate_limit,
        #     pacemaker.upper_rate_limit,
        #     pacemaker.fixed_av_delay,
        #     pacemaker.atrial_amplitude,
        #     pacemaker.ventricular_amplitude,
        #     pacemaker.atrial_pulse_width,
        #     pacemaker.ventricular_pulse_width
        #
        # ]

    def DDI(self,pacemaker):
        self.pace_atrium()
        self.pace_ventricle()
        self.sense_atrium()
        self.sense_ventricle()
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

    def DDD(self,pacemaker):
        self.pace_ventricle()
        self.pace_ventricle()
        self.sense_atrium()
        self.sense_ventricle()
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
    #
    # def AOOR():
    #     pass
    #
    # def AAIR():
    #     pass
    #
    # def VOOR():
    #     pass
    #
    # def VVIR():
    #     pass
    #
    # def VDDR():
    #     pass
    #
    # def DOOR():
    #     pass
    #
    # def DDIR():
    #     pass
    #
    # def DDDR():
    #     pass

    def pace_atrium(self,lower_rate_limit):
        interval = self.calc_interval(lower_rate_limit)
        return interval

    def pace_ventricle(self,lower_rate_limit):
        interval = self.calc_interval(lower_rate_limit)
        return interval


    @staticmethod
    def sense_atrium(data,heart_data,interval, p_wave, sense_type):
        has_pace = False
        p_wave_limit = 100

        # too slow / not sensed
        if heart_data < 60 or p_wave < data.atrial_sensitivity * p_wave_limit:
            interval = interval-data.atrial_pulse_width
            if sense_type == "trigger":
                sleep(max(interval,data.ARP)/1000)
                print("trigger",(max(interval,data.ARP)))
                has_pace = True
            else:
                sleep(max(interval,data.ARP,data.PVARP)/1000)

        # too fast
        # inhibit
        elif heart_data > 100:
            sleep(data.ARP/1000)
            print("too fast")
            has_pace = True
        # normal
        # continue sense
        else:
            sleep(data.ARP/1000)
            print("normal")
        return has_pace

    @staticmethod
    def sense_ventricle(data,heart_data, interval, r_wave, sense_type):
        r_wave_limit = 100
        # too slow / not sensed
        if heart_data < 60 or r_wave < data.ventricular_sensitivity * r_wave_limit:
            interval = interval-data.ventricular_pulse_width
            if sense_type == "trigger":
                sleep(max(interval,data.ARP)/1000)
                print("trigger",(max(interval,data.VRP,data.PVARP)))
            else:
                sleep(max(interval,data.VRP)/1000)
                print("inhibit")
        # too fast
        # inhibit
        elif heart_data > 100:
            sleep(data.VRP/1000)
            print("too fast")
        # normal
        # continue sense
        else:
            sleep(data.VRP/1000)
            print("normal")


    @staticmethod
    def trigger(amplitude,pulse_width):
        print(amplitude,pulse_width)
        return amplitude,pulse_width

    @staticmethod
    def inhibit(interval):
        sleep(interval)
    #
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