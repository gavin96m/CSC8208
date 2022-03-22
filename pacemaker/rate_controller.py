# RateController is used to calculate the impact on the battery when calling the sensing and pacing methods

import threading
import time
import Battery

# import lead

# corresponding abbreviation
A = "Atrial"
V = "Ventricular"
D = "Both"


class RateController(object):

    # run the sensing method
    def run_sensing(self, sense):
        print('Start calling the sensing method of this cycle...')
        # Call the static method to get the value of the chamber
        chamberChoose = sense.get_chamber(A)
        chamber = chamberChoose
        sense.add_sense(chamber)
        sensing_unit = RateController.consume_sensing(chamber)
        return sensing_unit
        print('End calling')

    # run the pacing method
    def run_pacing(self, pace):
        print('Start calling the pacing method of this cycle...')
        # Call the static method to get the value of the chamber
        chamberChoose = pace.get_chamber(A)
        chamber = chamberChoose
        pace.add_pace(chamber)
        mode = "AAT"
        # RateController.consume_pacing(mode)
        pacing_unit = RateController.consume_pacing(mode)
        return pacing_unit
        print('End calling')

    def get_interval(self):
        # Get the time interval between executing the sensing method and the pacing method
        print('The time interval is...')
        pass

    # The power consumed by executing a sensing method (based on different channels)
    # def consume_sensing(self):
    #     sensing_consume_dictionary = {'A': 0.005, 'V': 0.005, 'D': 0.005}
    #     sensing_consumed_unit = sensing_consume_dictionary.get(chamber)
    #     battery_sensing_consumed = battery_sensing_consumed - sensing_consumed_unit
    #     print(f'The battery consumed: {sensing_consumed_unit} mA.')
    #     return sensing_consumed_unit

    def consume_sensing(self, chamber):
        if chamber == "A":
            sensing_consumed_unit = 0.005
            print(f'The battery consumed: {sensing_consumed_unit} mA.')
            return sensing_consumed_unit
        elif chamber == "V":
            sensing_consumed_unit = 0.005
            print(f'The battery consumed: {sensing_consumed_unit} mA.')
            return sensing_consumed_unit
        elif chamber == "D":
            sensing_consumed_unit = 0.005
            print(f'The battery consumed: {sensing_consumed_unit} mA.')
            return sensing_consumed_unit

    # The power consumed by executing a pacing method (based on different modes)
    # def consume_pacing(self):
    #     pacing_consume_dictionary = {'AAT': 0.025, 'VVT': 0.025,
    #                                  'AOO': 0.025, 'AAI': 0.025,
    #                                  'VOO': 0.025, 'VVI': 0.025,
    #                                  'VDD': 0.038, 'DOO': 0.038,
    #                                  'DDI': 0.038, 'DDD': 0.038
    #                                  }
    #     pacing_consumed_unit = pacing_consume_dictionary.get(mode)
    #     battery_pacing_consumed = battery_pacing_consumed - pacing_consumed_unit
    #     print(f'The battery consumed: {pacing_consumed_unit} mA.')
    #     return pacing_consumed_unit

    def consume_pacing(self, mode):
        if mode == "AAT":
            pacing_consumed_unit = 0.025
            print(f'The battery consumed: {pacing_consumed_unit} mA.')
            return pacing_consumed_unit
        elif mode == "VVT":
            pacing_consumed_unit = 0.025
            print(f'The battery consumed: {pacing_consumed_unit} mA.')
            return pacing_consumed_unit
        elif mode == "AOO":
            pacing_consumed_unit = 0.025
            print(f'The battery consumed: {pacing_consumed_unit} mA.')
            return pacing_consumed_unit
        elif mode == "AAI":
            pacing_consumed_unit = 0.025
            print(f'The battery consumed: {pacing_consumed_unit} mA.')
            return pacing_consumed_unit
        elif mode == "VOO":
            pacing_consumed_unit = 0.025
            print(f'The battery consumed: {pacing_consumed_unit} mA.')
            return pacing_consumed_unit
        elif mode == "VVI":
            pacing_consumed_unit = 0.025
            print(f'The battery consumed: {pacing_consumed_unit} mA.')
            return pacing_consumed_unit
        elif mode == "VDD":
            pacing_consumed_unit = 0.038
            print(f'The battery consumed: {pacing_consumed_unit} mA.')
            return pacing_consumed_unit
        elif mode == "DOO":
            pacing_consumed_unit = 0.038
            print(f'The battery consumed: {pacing_consumed_unit} mA.')
            return pacing_consumed_unit
        elif mode == "DDI":
            pacing_consumed_unit = 0.038
            print(f'The battery consumed: {pacing_consumed_unit} mA.')
            return pacing_consumed_unit
        elif mode == "DDD":
            pacing_consumed_unit = 0.038
            print(f'The battery consumed: {pacing_consumed_unit} mA.')
            return pacing_consumed_unit


# instantiate the object
simulate_lead = lead.Lead()

# Launcher
sense = RateController()
pace = RateController()

# call methods in other classes
# By passing the lead class object c01 to the sense object
# the purpose of calling the test_lead method ventricular_Sensing() is achieved
sense.run_sensing(simulate_lead)
pace.run_pacing(simulate_lead)

# initial battery quantity
battery_size = 2000.0
# Current battery quantity
battery = 10.0
# set battery quantity
# battery = battery_size


while battery > 0:
    if 0.5 * battery_size < battery <= 1 * battery_size:
        print('The current power quantity is：%f \t' % battery)
        # set time interval
        time.sleep(1)
        # Call the sensing method in the lead class
        sensing_unit = sense.run_sensing(simulate_lead)
        # Select the power consumed by the channel corresponding to the sensing method
        battery = battery - sensing_unit
        # Use the data returned by the get_interval() method to change the parameter value
        time.sleep(1.12)
        # Call the pacing method in the lead class
        pacing_unit = pace.run_pacing(simulate_lead)
        # Select the power consumed by the mode corresponding to the pacing method
        battery = battery - pacing_unit
        # battery = battery - 0.02
        print('The remaining battery is: %f \t The remaining battery is sufficient\n' % battery)

    elif (0.5 * battery_size) >= battery > (0.2 * battery_size):
        print('Warning: The remaining battery is less than 50%!')
        # set time interval
        time.sleep(1)
        # Call the sensing method in the lead class
        sensing_unit = sense.run_sensing(simulate_lead)
        # Select the power consumed by the channel corresponding to the sensing method
        battery = battery - sensing_unit
        # Use the data returned by the get_interval() method to change the parameter value
        time.sleep(1.12)
        # Call the pacing method in the lead class
        pacing_unit = pace.run_pacing(simulate_lead)
        # Select the power consumed by the mode corresponding to the pacing method
        battery = battery - pacing_unit
        # battery = battery - 0.02
        print('The remaining power is: %f \n' % battery)

    elif (0.2 * battery_size) >= battery > (0.1 * battery_size):
        print('Warning2: The remaining power is less than 20%! Please pay attention to the battery power!')
        # set time interval
        time.sleep(1)
        # Call the sensing method in the lead class
        sensing_unit = sense.run_sensing(simulate_lead)
        # Select the power consumed by the channel corresponding to the sensing method
        battery = battery - sensing_unit
        # Use the data returned by the get_interval() method to change the parameter value
        time.sleep(1.12)
        # Call the pacing method in the lead class
        pacing_unit = pace.run_pacing(simulate_lead)
        # Select the power consumed by the mode corresponding to the pacing method
        battery = battery - pacing_unit
        # battery = battery - 0.02
        print('The remaining power is: %f \n' % battery)

    elif (0.1 * battery_size) >= battery > 0:
        print('Warning: The remaining power is less than 10%! '
              'Please replace the battery or charge it as soon as possible!')
        # set time interval
        time.sleep(1)
        # Call the sensing method in the lead class
        sensing_unit = sense.run_sensing(simulate_lead)
        # Select the power consumed by the channel corresponding to the sensing method
        battery = battery - sensing_unit
        # Select the power consumed by the channel corresponding to the sensing method
        time.sleep(1.12)
        # Call the pacing method in the lead class
        pacing_unit = pace.run_pacing(simulate_lead)
        # Select the power consumed by the mode corresponding to the pacing method
        battery = battery - pacing_unit
        # battery = battery - 0.02
        print('The remaining power is: %f \n' % battery)
        print('Emergency: battery drained!!!')
