import _thread
from time import sleep
import IO
from heart_controller import HeartController

def AAT(self, data: IO):
    # data.lower_rate_limit
    # data.upper_rate_limit
    # data.atrial_amplitude
    # data.atrial_pulse_width
    # data.atrial_sensitivity,
    # data.ARP,
    # data.PVARP
    interval = HeartController.pace_atrium(data.lower_rate_limit)
    # todo get P_wave
    p_wave = 110
    has_sense = HeartController.sense_atrium(data, interval, p_wave, "trigger")
    if not has_sense:
        HeartController.trigger(data.atrial_amplitude, data.atrial_pulse_width)
        sleep((interval-data.atrial_pulse_width-data.ARP)/1000)
    # has_sense
    else:
        sleep(interval/1000)
    return data.atrial_amplitude, data.atrial_pulse_width


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

def VVT(self, data: IO):
    # pacemaker.lower_rate_limit,
    # pacemaker.upper_rate_limit,
    # pacemaker.ventricular_amplitude,
    # pacemaker.ventricular_pulse_width,
    # pacemaker.ventricular_sensitivity,
    # pacemaker.VRP
    interval = HeartController.pace_ventricular(data.lower_rate_limit)
    # todo get r_wave
    r_wave = 110
    has_sense = HeartController.sense_ventricular(data, interval, r_wave, "trigger")
    if not has_sense:
        self.trigger(data.ventricular_amplitude, data.ventricular_pulse_width)
        sleep((interval-data.ventricular_pulse_width-data.ARP)/1000)
    # has_sense
    else:
        sleep(interval / 1000)
    return data.ventricular_amplitude, data.ventricular_pulse_width

def AOO(self, data: IO):
    # pacemaker.lower_rate_limit,
    # pacemaker.upper_rate_limit,
    # pacemaker.atrial_amplitude,
    # pacemaker.atrial_pulse_width,

    interval = self.pace_atrium(data.lower_rate_limit) - data.atrial_pulse_width
    sleep(interval / 1000)
    print(data.atrial_amplitude, data.atrial_pulse_width)
    return data.atrial_amplitude, data.atrial_pulse_width

    # return li
    # todo 两个参数（a_amplitude,a_pulse_width)


def AAI(self, data):
    #     pacemaker.lower_rate_limit,
    #     pacemaker.upper_rate_limit,
    #     pacemaker.atrial_amplitude,
    #     pacemaker.atrial_pulse_width,
    #     pacemaker.atrial_sensitivity,
    #     pacemaker.ARP,
    #     pacemaker.PVARP,
    #     pacemaker.hysteresis,
    #     pacemaker.rate_smoothing
    interval = HeartController.pace_atrium(data.lower_rate_limit)
    # todo get p_wave
    p_wave = 1000
    has_sense = HeartController.sense_atrium(data, interval, p_wave, "inhibit")
    if has_sense:
        # no hysteresis
        if not data.hysteresis:
        #     inhibit(pulse_width):
            HeartController.inhibit(data.atrial_pulse_width)
        # hysteresis
        else:
#            inhibit(pulse_width,hysteresis,hate_rate):
            HeartController.inhibit(data.atrial_pulse_width,data.hysteresis,data.hate_rate)
    else:
        return data.pulse_width,data.hysteresis


def VOO(self, data: IO):
    # pacemaker.lower_rate_limit,
    # pacemaker.upper_rate_limit,
    # pacemaker.ventricular_amplitude,
    # pacemaker.ventricular_pulse_width
    interval = self.pace_ventricular(data.lower_rate_limit) - data.ventricular_pulse_width
    sleep(interval / 1000)
    print(data.ventricular_amplitude, data.ventricular_pulse_width)
    return data.ventricular_amplitude, data.ventricular_pulse_width


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


def VDD(self, pacemaker):
    self.pace_ventricular()
    self.sense_ventricular()
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


def DOO(self, data):
    try:
        _thread.start_new_thread(self.AOO, (data,))
        _thread.start_new_thread(self.VOO, (data,))
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