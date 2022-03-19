# @Time    : 2022-03-12 1:55 a.m.
# @Author  : Xiaoxia Li
# @FileName: test.py
# @Software: PyCharm
# Description: a basic class for lead object
class LeadObject():

    def __init__(self,electrode, atrial_lead, ventricular_lead):
        self.electrode = electrode
        self.atrial_lead = atrial_lead
        self.ventricular_lead = ventricular_lead

    @property  # getter
    def electrode(self):
        return self.electrode

    @electrode.setter
    def electrode(self, electrode):
        self.electrode = electrode

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

    # toString
    def __str__(self):
        return "%s: %s %s " % ( self.electrode, self.atrial_lead, self.ventricular_lead)#


s2 = LeadObject('TTJ', 'YYT', 'pp')
s2.electrode = 'TT'

print(s2)
