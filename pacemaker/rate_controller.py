# RateController is used to calculate the impact on the battery when calling the sensing and pacing methods

import threading
import time

# import lead

# corresponding abbreviation
from pacemaker.lead import LeadController


class Battery(object):

    def __init__(self, quantity):

        self.quantity = quantity

    # init battery 2000
    @staticmethod
    def quantity():
        return 2000

    # battery consumption for each mode per time
    @staticmethod
    def battery_consumption_mode(mode):
        consumption = {'AAT': 0.025, 'VVT': 0.025, 'AOO': 0.025, 'AAI': 0.025,
                       'VOO': 0.025, 'VVI': 0.025, 'DOO': 0.038,}
        return consumption[mode]

    # if single mode < 200. or dual mode < 300, send alarm
    def battery_low_alarm(self, mode):
        if mode in ['AAT', 'VVT', 'AOO', 'AAI', 'VOO', 'VVI'] and self.quantity() < 200:
            return 'Please replace the battery'
        if mode in ['DOO'] and self.quantity() < 300:
            return 'Please replace the battery'

    # if dual mode has a lower battery, switch to single mode automatically
    def battery_low_change(self, mode):
        if mode == 'DOO' and self.quantity() < 300:
            return mode == 'VOO'
        elif mode == 'DDD' and self.quantity() < 300:
            return mode == 'VVI'

    # calculate battery consumption per time based on mode
    def battery_consumption(self, mode):
        mode_consumption = self.battery_consumption_mode(mode)
        battery_left = self.quantity() - mode_consumption
        print(f'The battery consumed: {mode_consumption} mA.')
        self.battery_low_alarm(self, mode)
        self.battery_low_change(self, mode)
        return battery_left

class RateController(object):

    # run the sensing method
    @staticmethod
    def run_sensing(LeadController,chamber):
        print('Start calling the sensing method of this cycle...')
        # Call the static method to get the value of the chamber
        chamber_choose = LeadController.get_chamber(LeadController,chamber)
        chamber = chamber_choose
        # sense.add_sense(chamber)
        sensing_unit = RateController.consume_sensing(LeadController,chamber)
        return sensing_unit
        print('End calling')

    # run the pacing method
    @staticmethod
    def run_pacing(LeadController, chamber):
        print('Start calling the pacing method of this cycle...')
        # Call the static method to get the value of the chamber
        chamber_choose = LeadController.get_chamber(LeadController,chamber)
        chamber = chamber_choose
        # pace.add_pace(chamber)
        mode = "AAT"
        # RateController.consume_pacing(mode)
        pacing_unit = RateController.consume_pacing(LeadController, mode)
        return pacing_unit
        print('End calling')

    # battery consumption for sense
    def consume_sensing(self, chamber):
        if chamber == LeadController.get_chamber_a():
            sensing_consumed_unit = 0.005
            print(f'The battery consumed: {sensing_consumed_unit} mA.')
            return sensing_consumed_unit
        elif chamber == LeadController.get_chamber_v():
            sensing_consumed_unit = 0.005
            print(f'The battery consumed: {sensing_consumed_unit} mA.')
            return sensing_consumed_unit
        elif chamber == LeadController.get_chamber_d():
            sensing_consumed_unit = 0.005
            print(f'The battery consumed: {sensing_consumed_unit} mA.')
            return sensing_consumed_unit

    # battery consumption for pacing
    def consume_pacing(self, mode):
        pacing_consumed_unit = Battery.battery_consumption_mode(mode)
        print(f'The battery consumed: {pacing_consumed_unit} mA.')
        return pacing_consumed_unit


if __name__ == '__main__':

    simulate_lead = LeadController
    print(LeadController.get_chamber(simulate_lead,"Atrial"))
    # instantiate the object


    # Launcher
    sense = RateController()
    pace = RateController()

    # call methods in other classes
    # By passing the lead class object c01 to the sense object
    # the purpose of calling the test_lead method ventricular_Sensing() is achieved
    sense.run_sensing(LeadController,"Atrial")
    pace.run_pacing(simulate_lead,"Ventricular")

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
            sensing_unit = sense.run_sensing(simulate_lead,"Atrial")
            print(type(sensing_unit))
            # Select the power consumed by the channel corresponding to the sensing method
            battery = battery - sensing_unit
            # Select the power consumed by the channel corresponding to the sensing method
            time.sleep(1.12)
            # Call the pacing method in the lead class
            pacing_unit = pace.run_pacing(simulate_lead, "Ventricular")
            # Select the power consumed by the mode corresponding to the pacing method
            battery = battery - pacing_unit
            # battery = battery - 0.02
            print('The remaining power is: %f \n' % battery)
            print('Emergency: battery drained!!!')