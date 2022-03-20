# @Time    : 2022-03-12 1:55 a.m.
# @Author  : Xiaoxia Li
# @FileName: test.py
# @Software: PyCharm
# Description: a basic class for lead object
class Lead():

    def __init__(self, atrial_lead, ventricular_lead, resistance):

        self.resistance = resistance
        self.atrial_lead = atrial_lead
        self.ventricular_lead = ventricular_lead

    @property  # getter
    def atrial_lead(self):
        return self.atrial_lead

    @atrial_lead.setter
    def atrial_lead(self, atrial_lead):
        self.atrial_lead = atrial_lead

    @property  # getter
    def ventricular_lead(self):
        return self.ventricular_lead

    @ventricular_lead.setter
    def ventricular_lead(self, ventricular_lead):
        self.ventricular_lead = ventricular_lead

    @property  # getter
    def resistance(self):
        return self.resistance

    @resistance.setter
    def resistance(self, resistance):
        self.resistance = 100

    # toString
    def __str__(self):
        return "%s: %s %s" % (self.atrial_lead, self.ventricular_lead, self.resistance)#


s2 = Lead('TTJ', 'YYT', 'pp')
s2.electrode = 'TT'

print(s2)
