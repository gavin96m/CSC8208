from urllib import response
from numpy import char
import heart_controller, lead, rate_controller, Battery

class Pacemaker:
    _accelerometer = False
    paced = char
    sense = char
    response = char

    lead_atrial_sensing = False
    lead_ventricle_sensing = False
    lead_atrial_pacing = False
    lead_ventricle_pacing = False
    trigger_response = False
    inhibit_response = False

    def __init__(self, paced, sensed, response):
        self.paced = paced
        self.sense = sensed
        self.response = response

        self.heart_controller = heart_controller.HearController()
        self.rate_controller = rate_controller.RateController()
        self.battery = Battery.Battery()

        if(paced == 'A' or paced == 'D'):
            self.lead_atrial_pacing = lead.Lead.atrial_Pacing()
        
        if(paced == 'V'):
            self.lead_ventricle_pacing = lead.Lead.ventricular_Pacing()
        
        if(sensed == 'A' or paced == 'D'):
            self.lead_atrial_sensing = lead.Lead.atrial_Sensing()

        if(sensed == 'V'):
            self.lead_ventricle_pacing == lead.Lead.ventricular_Pacing()

        if(response == 'I' or response == 'D'):
            self.inhibit_response = lead.Lead.inhibit_Response()

        if(response == 'T'):
            self.trigger_response = lead.Lead.trigger_Response()

    def get_info(self):
        return(self.paced, self.sense, self.response)

    