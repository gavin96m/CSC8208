from urllib import response
from numpy import char
import rate_controller, Battery, json

class Pacemaker:
    _accelerometer = False
    paced = char
    sense = char
    response = char
    mode = str

    lead_atrial_sensing = False
    lead_ventricle_sensing = False
    lead_atrial_pacing = False
    lead_ventricle_pacing = False
    trigger_response = False
    inhibit_response = False

    def __init__(self):
        settings = self.load_settings("111")
        mode = settings['paceMode']
        modes = self.splits(mode)
        self.paced = modes[0]
        self.sense = modes[1]
        self.response = mode[2]

        self.rate_controller = rate_controller.RateController()
        self.battery = Battery.Battery("AAT")

    
        """
        TODO Fix creating leads
        if(self.paced == 'A' or self.paced == 'D'):
            self.lead_atrial_pacing = lead.Lead.atrial_Pacing()
        
        if(self.paced == 'V'):
            self.lead_ventricle_pacing = lead.Lead.ventricular_Pacing()
        
        if(self.sensed == 'A' or self.paced == 'D'):
            self.lead_atrial_sensing = lead.Lead.atrial_Sensing()

        if(self.sensed == 'V'):
            self.lead_ventricle_pacing == lead.Lead.ventricular_Pacing()

        if(self.response == 'I' or self.response == 'D'):
            self.inhibit_response = lead.Lead.inhibit_Response()

        if(self.response == 'T'):
            self.trigger_response = lead.Lead.trigger_Response()"""


    def advance(self):
        self.battery.consume()
        print(f'current remaining power：{self.battery.quantity} mA')
        #TODO Add ending or message if it runs out

    def get_info(self):
        return(self.paced, self.sense, self.response)

    def splits(self, s):
        return [char for char in s]

    def load_settings(self, user):
        """Gets the users setting from the json file"""
        f = open("user/"+user+'.json')
        data = json.load(f)
        return data