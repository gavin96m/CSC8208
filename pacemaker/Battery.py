# coding=u8
import time


class Battery(object):

    def __init__(self, mode):
        self.mode = mode
        self._quantity = 2000

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def consume(self):
        speed_lookup = {'AAT': 0.025, 'VVT': 0.025, 'AOO': 0.025, 'AAI': 0.025, 'VOO': 0.025, 'VVI': 0.025, 'VDD': 0.038, 'DOO': 0.038, 'DDI': 0.038,
                        'DDD': 0.038}
        unit = speed_lookup.get(self.mode)
        self.quantity = self.quantity - unit
        print(f'The battery consumed: {unit} mA.')
        return self.quantity


if __name__ == '__main__':
    b1 = Battery(mode='AAT')
    quantity = b1.quantity

    while quantity > 0:
        time.sleep(1)
        quantity = b1.consume()
        print(f'current remaining power：{quantity} mA')
