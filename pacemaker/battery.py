# coding=u8
import time


class Battery(object):

    def __init__(self, mode):
        self.mode = mode
        self._quantity = 2000

    # init battery 2000
    @staticmethod
    def quantity():
        return 2000

    # battery consumption for each mode per time
    @staticmethod
    def battery_consumption_mode(mode):
        consumption = {'AAT': 0.025, 'VVT': 0.025, 'AOO': 0.025, 'AAI': 0.025,
                       'VOO': 0.025, 'VVI': 0.025, 'DOO': 0.038,
                       'DDI': 0.038, 'DDD': 0.038}
        return consumption[mode]

    # if single mode < 200. or dual mode < 300, send alarm
    def battery_low_alarm(self, mode):
        if mode in ['AAT', 'VVT', 'AOO', 'AAI', 'VOO', 'VVI'] and self.quantity() < 200:
            return 'Please replace the battery'
        if mode in ['DOO', 'DDI', 'DDD'] and self.quantity() < 300:
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


def main():
    while Battery.quantity() > 0:
        time.sleep(1)
        quantity = Battery.battery_consumption(Battery, "VVT")
        print(f'current remaining power：{quantity} mA')


if __name__ == '__main__':
    main()

