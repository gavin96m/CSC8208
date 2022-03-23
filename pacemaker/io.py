#!/usr/bin/env python
# coding: utf-8

import json
# In[5]:

str_file = "../user/111.json"

class IO:
    @staticmethod
    def read_file(str_file):
        with open(str_file, 'r') as f:
            # print("Load str file from {}".format(str_file))
            # print(json.load(f))
            data = json.load(f)
        return data

    @staticmethod
    def handle_data(data):
        update_data = {}
        update_data["paceMode"]= data["paceMode"]
        update_data["lower_rate_limit"]= int(data["entry01"])
        update_data["upper_rate_limit"]= int(data["entry02"])
        update_data["fixed_AV_delay"]= int(data["entry04"])
        update_data["dynamic_AV_delay"]= IO.set_bool(data["entry05"])
        update_data["sensed_AV_delay_offset"]= IO.set_bool_or_int(data["entry07"])
        update_data["atrial_amplitude"]= IO.set_bool_or_float(data["entry08"])
        update_data["ventricular_amplitude"]= IO.set_bool_or_float(data["entry09"])
        update_data["atrial_pulse_width"]= float(data["entry12"])
        update_data["ventricular_pulse_width"]= float(data["entry13"])
        update_data["atrial_sensitivity"]= float(data["entry14"])
        update_data["ventricular_sensitivity"]= float(data["entry15"])
        update_data["VRP"]= int(data["entry16"])
        update_data["ARP"]= int(data["entry17"])
        update_data["PVARP"]= int(data["entry18"])
        update_data["PVARP_extension"]= IO.set_bool_or_int(data["entry19"])
        update_data["hysteresis"]= IO.set_bool_or_int(data["entry20"])
        update_data["rate_smoothing"]= IO.set_bool_or_float(data["entry21"])
        update_data["ATR_duration"]= int(data["entry22"])
        update_data["ATR_fallback_mode"]= IO.set_bool(data["entry23"])
        update_data["ATR_fallback_time"]= int(data["entry24"])
        update_data["reaction_time"]= int(data["entry27"])
        update_data["response_factor"]= int(data["entry28"])
        update_data["recovery_time"]= int(data["entry29"])
        update_data["atrial_blanking"] = int(data["entry26"])
        update_data["ventricular_blanking"] = int(data["entry25"])
        return update_data

    @staticmethod
    def set_bool(param):
        if(param) == "ON":
            return False
        else:
            return True

    @staticmethod
    def set_bool_or_int(param):
        if(param) == "OFF":
            return False
        else:
            return int(param)

    @staticmethod
    def set_bool_or_float(param):
        if(param) == "OFF":
            return False
        else:
            return float(param)

    @staticmethod
    def get_data(str_file):
        data_dict = IO.read_file(str_file)
        data = IO.handle_data(data_dict)
        return data



print(IO.get_data("../user/111.json"))



