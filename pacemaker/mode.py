# from parameters import Parameters
class Mode:

    mode = ["AOO", "VOO", ""]
    def AAT(pacemaker):
     return [
    pacemaker.lower_rate_limit,
    pacemaker.upper_rate_limit,
    pacemaker.atrial_amplitude,
    pacemaker.atrial_pulse_width,
    pacemaker.atrial_sensitivity,
    pacemaker.ARP,
    pacemaker.PVARP
    ]

def VVT(pacemaker):
    return [
    pacemaker.lower_rate_limit,
    pacemaker.upper_rate_limit,
    pacemaker.ventricular_amplitude,
    pacemaker.ventricular_pulse_width,
    pacemaker.ventricular_sensitivity,
    pacemaker.VRP
    ]

def AOO(pacemaker):
    return [
    pacemaker.lower_rate_limit,
    pacemaker.upper_rate_limit,
    pacemaker.atrial_amplitude,
    pacemaker.atrial_pulse_width,
    ]


    # lower rate limit, upper rate limit, atrial amplitude, atrial pulse width
    # li = []
    # li.append(Parameters.change_lrl(lower_rate_limit))
    # set_max_pacing_interval(?)
    # # 应该定义起搏间隔（没hysteresis）
    # li.append(Parameters.change_url(upper_rate_limit))
    # set_min_pacing_interval(?)
    # li.append(Parameters.change_aa(atrial_amplitude))
    # # todo 间隔时间
    # li.append(Parameters.change_apw(atrial_pulse_width))
    return li
    # todo 两个参数（a_amplitude,a_pulse_width)


def AAI(pacemaker):
    return [
    pacemaker.lower_rate_limit,
    pacemaker.upper_rate_limit,
    pacemaker.atrial_amplitude,
    pacemaker.atrial_pulse_width,
    pacemaker.atrial_sensitivity,
    pacemaker.ARP,
    pacemaker.PVARP,
    pacemaker.hysteresis,
    pacemaker.rate_smoothing
    ]

def VOO(pacemaker):
    return [
    pacemaker.lower_rate_limit,
    pacemaker.upper_rate_limit,
    pacemaker.ventricular_amplitude,
    pacemaker.ventricular_pulse_width
    ]

def VVI(pacemaker):
    return [
    pacemaker.lower_rate_limit,
    pacemaker.upper_rate_limit,
    pacemaker.ventricular_amplitude,
    pacemaker.ventricular_pulse_width,
    pacemaker.ventricular_sensitivity,
    pacemaker.VRP,
    pacemaker.hysteresis,
    pacemaker.rate_smoothing,
    ]

def VDD(pacemaker):
    return [
    pacemaker.lower_rate_limit,
    pacemaker.upper_rate_limit,
    pacemaker.fixed_AV_delay,
    pacemaker.dynamic_AV_delay,
    pacemaker.ventricular_amplitude,
    pacemaker.ventricular_pulse_width,
    pacemaker.VRP,
    pacemaker.PVARP_extension,
    pacemaker.rate_smoothing,
    pacemaker.atr_duration,
    pacemaker.atr_fallback_mode,
    pacemaker.atr_fallback_time
    ]
    pass


def DOO(pacemaker):
    return [
    pacemaker.lower_rate_limit,
    pacemaker.upper_rate_limit,
    pacemaker.fixed_av_delay,
    pacemaker.atrial_amplitude,
    pacemaker.ventricular_amplitude,
    pacemaker.atrial_pulse_width,
    pacemaker.ventricular_pulse_width

    ]

def DDI(pacemaker):
    return [
        pacemaker.lower_rate_limit,
        pacemaker.upper_rate_limit,
        pacemaker.fixed_AV_delay,
        pacemaker.atrial_amplitude,
        pacemaker.ventricular_amplitude,
        pacemaker.atrial_pulse_width,
        pacemaker.ventricular_pulse_width,
        pacemaker.atrial_sensitivity,
        pacemaker.ventricular_sensitivity,
        pacemaker.VRP,
        pacemaker.ARP,
        pacemaker.PVARP,
    ]


def DDD(pacemaker):
    return [
        pacemaker.lower_rate_limit,
        pacemaker.upper_rate_limit,
        pacemaker.fixed_AV_delay,
        pacemaker.dynamic_AV_delay,
        pacemaker.sensed_av_delay_offset,
        pacemaker.atrial_amplitude,
        pacemaker.ventricular_amplitude,
        pacemaker.atrial_pulse_width,
        pacemaker.ventricular_pulse_width,
        pacemaker.atrial_sensitivity,
        pacemaker.ventricular_sensitivity,
        pacemaker.VRP,
        pacemaker.ARP,
        pacemaker.PVARP,
        pacemaker.PVARP_extension,
        pacemaker.hysteresis,
        pacemaker.rate_smoothing,
        pacemaker.atr_duration,
        pacemaker.atr_fallback_mode,
        pacemaker.atr_fallback_time
    ]
    pass


def AOOR():
    pass


def AAIR():
    pass


def VOOR():
    pass


def VVIR():
    pass



def VDDR():
    pass




def DOOR():
    pass


def DDIR():
    pass

def DDDR():
    pass


