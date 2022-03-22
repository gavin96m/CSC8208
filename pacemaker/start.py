import threading
import time
from time import sleep
from heart_controller import PacemakerBasic as Pacemaker
from heart_controller import PacemakerController
from lead import LeadController
from lead import Lead
from heart import HeartConfig

# lower_rate_limit
lrl = 60
data = {
    "lower_rate_limit":60,
    "upper_rate_limit":120,
    "fixed_AV_delay":150,
    "dynamic_AV_delay":"OFF",
    "sensed_AV_delay_offset":"OFF",
    "atrial_amplitude":3.5,
    "ventricular_amplitude":3.5,
    "atrial_pulse_width":0.4,
    "ventricular_pulse_width":0.4,
    "atrial_sensitivity":0.75,
    "ventricular_sensitivity":2.5,
    "VRP":320,
    "ARP":250,
    "PVARP":250,
    "PVARP_extension":"OFF",
    "hysteresis":"OFF",
    "rate_smoothing":"OFF",
    "ATR_duration":20,
    "ATR_fallback_mode":"OFF",
    "ATR_fallback_time":1,
    "a_blacking_period":30,
    "v_blacking_period":30
}


def AOO_start(pacemaker_obj,lead_a):

    while True:
        pacemaker_controller.AOO(pacemaker_obj,lead_a)

def VOO_start(pacemaker_obj,lead_v):
    while True:
        pacemaker_controller.VOO(pacemaker_obj,lead_v)

# def AAT_start(lead_a:LeadController,event_obj,lower_rate_limit,time=0):
def AAT_start(pacemaker_obj,lead_a,lower_rate_limit,evnet_obj):
    interval = 60000 / lower_rate_limit
    while True:
        sense = event_obj.wait()
        if sense:
            print("sense now, reset the time")
            break
        # else:
        #     amplitude,width = AAT()
        #     lead_a.stimulate_a(pulse_info=[amplitude,width])
        start = time.time()
        sense = event_obj.wait(interval/1000)
        # mode.AAT(data,lead_v)



def receive_p(lead_a:LeadController,event_obj:threading.Event,heart_config:HeartConfig):
    row = 0
    while row < 15:
        lead_a.transit_heart_info_p(heart_config,row)
        # send p after pp
        sleep(lead_a.transit_heart_info_pp(heart_config,row))
        # send signal
        event_obj.set()
        # close
        event_obj.clear()


print("87")
lead_a = LeadController()
lead_v = LeadController()
pacemaker_obj = Pacemaker(data)
pacemaker_controller = PacemakerController()
lower_rate_limit = 60

# AOO
# AOO_start(pacemaker_obj,lead_a)

# VOO
# VOO_start(pacemaker_obj,lead_v)


# AAT
# initialising
event_obj = threading.Event()
heart_config = HeartConfig()

# start

# generate
# event_obj.set()

thread1 = threading.Thread(target=AAT_start, args=(pacemaker_obj,lead_a,lower_rate_limit,event_obj))
thread2 = threading.Thread(target=receive_p, args=(event_obj, 5, heart_config))
thread1.start()
thread2.start()