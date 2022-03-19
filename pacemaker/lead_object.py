# @Time    : 2022-03-12 1:55 a.m.
# @Author  : Xiaoxia Li
# @FileName: test.py
# @Software: PyCharm
class Lead_Object(object):

    def __init__(self, Anode, Cathode, Electrode, Atrial_lead, Ventricular_lead):#
        self.Anode = Anode
        self.Cathode = Cathode
        self.Electrode = Electrode
        self.Atrial_lead = Atrial_lead
        self.Ventricular_lead = Ventricular_lead

    @property  # getter
    def anode(self):
        return self.Anode

    @anode.setter
    def anode(self, Anode):
        self.Anode = Anode

    @property  # getter
    def cathode(self):
        return self.Cathode

    @cathode.setter
    def cathode(self, Cathode):
        self.Cathode = Cathode

    @property  # getter
    def electrode(self):
        return self.Electrode

    @electrode.setter
    def electrode(self, Electrode):
        self.Electrode = Electrode

    @property  # getter
    def atrial_lead(self):
        return self.Atrial_lead

    @atrial_lead.setter
    def atrial_lead(self, Atrial_lead):
        self.Atrial_lead = Atrial_lead

    @property  # getter
    def ventricular_lead(self):
        return self.Ventricular_lead

    @ventricular_lead.setter
    def ventricular_lead(self, Ventricular_lead):
        self.Ventricular_lead = Ventricular_lead

    # toString
    def __str__(self):
        return "%s: %s %s %s %s" % (self.Anode, self.Cathode, self.Electrode, self.Atrial_lead, self.Ventricular_lead)#


s2 = Lead_Object('Tom', 'Jerry', 'TTJ', 'YYT', 'pp')
s2.Anode = 'TT'
s2.Cathode = 'JJ'

print(s2)
