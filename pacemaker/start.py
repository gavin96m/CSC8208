import threading
import time
from time import sleep
from heart_controller import PacemakerBasic as Pacemaker
from heart_controller import HeartController as PacemakerController
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
    "v_blacking_period":30,
}

class pacemaker():

    @staticmethod
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

            row += 1

    @staticmethod
    def receive_r(lead_v:LeadController,event_obj:threading.Event,heart_config:HeartConfig):
        row = 0
        while row < 15:
            lead_v.transit_heart_info_r(heart_config, row)
            # send p after pp
            sleep(lead_v.transit_heart_info_rr(heart_config, row))
            # send signal
            event_obj.set()
            # close
            event_obj.clear()

            row += 1

    @staticmethod
    def AOO_start(pacemaker_obj, lead_a):

        while True:
            pacemaker_controller.AOO(pacemaker_obj, lead_a)

    @staticmethod
    def VOO_start(pacemaker_obj, lead_v):
        while True:
            pacemaker_controller.VOO(pacemaker_obj, lead_v)

    @staticmethod
    def AAT_start(pacemaker_obj: Pacemaker, lead_a, lower_rate_limit, event_obj):
        interval = 60000 / lower_rate_limit
        row = 0
        while row < 15:
            sleep(pacemaker_obj.a_blacking_period)
            start = time.time()
            p_wave = event_obj.wait(interval - pacemaker_obj.a_blacking_period - pacemaker_obj.atrial_pulse_width)
            if p_wave:
                now = time.time()
                # 0:between ARP, 1:sense P ,2:no sense
                status_code = pacemaker_controller.AAT(pacemaker_obj, lead_a,
                                                       lead_a.transit_heart_info_p(heart_config, row), now - start)
                # between ARP
                if status_code == 0:
                    print("between ARP, it may be noise.")
                    continue
                # sense
                elif status_code == 1:
                    print("sense, reset the time")
                    break
            # no sense
            else:
                pulse_info = [pacemaker_obj.atrial_amplitude, pacemaker_obj.atrial_pulse_width]
                pacemaker_obj.trigger(lead_a, pulse_info)
                print(pulse_info)

            row += 1

    @staticmethod
    def VVT_start(pacemaker_obj: Pacemaker, lead_v, lower_rate_limit, event_obj):
        interval = 60000 / lower_rate_limit
        row = 0
        while row < 15:
            sleep(pacemaker_obj.v_blacking_period)
            start = time.time()
            r_wave = event_obj.wait(interval - pacemaker_obj.v_blacking_period - pacemaker_obj.ventricular_pulse_width)
            if r_wave:
                now = time.time()
                # 0:between ARP, 1:sense P ,2:no sense
                status_code = pacemaker_controller.VVT(pacemaker_obj, lead_v,
                                                       lead_v.transit_heart_info_r(heart_config, row), now - start)
                # between ARP
                if status_code == 0:
                    print("between VRP, it may be noise.")
                    continue
                # sense
                elif status_code == 1:
                    print("sense, reset the time")
                    break
            # no sense
            else:
                pulse_info = [pacemaker_obj.ventricular_amplitude, pacemaker_obj.ventricular_pulse_width]
                pacemaker_obj.trigger(lead_v, pulse_info)
                print(pulse_info)

            row += 1

    @staticmethod
    def AAI_start(pacemaker_obj: Pacemaker, lead_a, lower_rate_limit, event_obj):
        interval = 60000 / lower_rate_limit
        row = 0
        while row < 15:
            sleep(pacemaker_obj.a_blacking_period)
            start = time.time()
            p_wave = event_obj.wait(interval - pacemaker_obj.a_blacking_period - pacemaker_obj.atrial_pulse_width)
            if p_wave:
                now = time.time()
                # 0:between ARP, 1:sense P ,2:no sense
                status_code = pacemaker_controller.AAI(pacemaker_obj, lead_a,
                                                       lead_a.transit_heart_info_p(heart_config, row), now - start)
                # between ARP
                if status_code == 0:
                    print("between VRP, it may be noise.")
                    continue
                # sense
                elif status_code == 1:
                    print("sense, reset the time")
                    break
            # no sense
            else:
                pulse_info = [pacemaker_obj.atrial_amplitude, pacemaker_obj.atrial_pulse_width]
                pacemaker_obj.trigger(lead_a, pulse_info)
                print(pulse_info)

            row += 1


def set_mode(self,mode):
        if mode == "AOO":
            self.AOO_start(pacemaker_obj, lead_a)

        elif mode == "VOO":
            self.VOO_start(pacemaker_obj,lead_v)

        elif mode == "AAT":
            thread1 = threading.Thread(target=self.receive_p, args=(pacemaker_obj,lead_a,lower_rate_limit,event_obj))
            thread2 = threading.Thread(target=self.AAT_start, args=(lead_a,event_obj,heart_config))

            thread1.start()
            thread2.start()

        elif mode == "VVT":
            thread1 = threading.Thread(target=self.receive_r, args=(pacemaker_obj, lead_v, lower_rate_limit, event_obj))
            thread2 = threading.Thread(target=self.VVT_start, args=(lead_v, event_obj, heart_config))

            thread1.start()
            thread2.start()

        elif mode == "AAI":
            thread1 = threading.Thread(target=self.receive_p, args=(pacemaker_obj, lead_a, lower_rate_limit, event_obj))
            thread2 = threading.Thread(target=self.AAI_start, args=(lead_a, event_obj, heart_config))

            thread1.start()
            thread2.start()

        elif mode == "VVI":
            thread1 = threading.Thread(target=self.receive_r, args=(pacemaker_obj, lead_v, lower_rate_limit, event_obj))
            thread2 = threading.Thread(target=self.VVI_start, args=(lead_v, event_obj, heart_config))

            thread1.start()
            thread2.start()

#         elif mode == "DDD":
# #             TODO




lead_a = LeadController()
lead_v = LeadController()
pacemaker_obj = Pacemaker(data)
pacemaker_controller = PacemakerController()
lower_rate_limit = 60



# AAT
# initialising
event_obj = threading.Event()
heart_config = HeartConfig()

# start


# generate
# event_obj.set()
#
# thread1 = threading.Thread(target=AAT_start, args=(pacemaker_obj,lead_a,lower_rate_limit,event_obj))
# thread2 = threading.Thread(target=receive_p, args=(event_obj, 5, heart_config))
# thread1.start()
# thread2.start()
set_mode("AAT")