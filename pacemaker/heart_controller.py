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

    def pace_atrium(self,lower_rate_limit):
        interval = self.calc_interval(lower_rate_limit)
        return interval

    def pace_ventricular(self,lower_rate_limit):
        interval = self.calc_interval(lower_rate_limit)
        return interval



    def sense_atrium(data:IO,interval, p_wave, sense_type):
        has_sense = False

        # not sensed
        if p_wave < data.atrial_sensitivity:
            interval = interval-data.atrial_pulse_width
            if sense_type == "trigger":
                # sleep(max(interval,data.ARP)/1000)
                sleep(data.ARP/1000)
                print("trigger",data.ARP)
            else:
                sleep(max(data.ARP,data.PVARP)/1000)
                print("inhibit",data.ARP)

        # normal
        # continue sense
        else:
            # sleep(data.ARP/1000)
            sleep(interval/1000)
            print("normal")
            has_sense = True
        return has_sense


    def sense_ventricular(data, interval, r_wave, sense_type):
        has_sense = False
        # too slow / not sensed
        if r_wave < data.ventricular_sensitivity:
            interval = interval-data.ventricular_pulse_width
            if sense_type == "trigger":
                sleep(max(data.VRP,data.PVARP)/1000)
                print("trigger",(max(data.VRP,data.PVARP)))
            # inhibit
            else:
                sleep(data.VRP/1000)
                print("inhibit")
        # inhibit
        # normal
        # continue sense
        else:
            print("normal")
            has_sense = True
        return has_sense



    def trigger(amplitude,pulse_width):
        print(amplitude,pulse_width)
        sleep(pulse_width/1000)
        # TODO: send to lead
        return amplitude,pulse_width

    # hystersis is OFF
    def inhibit(pulse_width):

        print(pulse_width)
        sleep(pulse_width/1000)
        # TODO: send NONE to lead

    # hysteresis is not OFF
    def inhibit(pulse_width,hysteresis,hate_rate):
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