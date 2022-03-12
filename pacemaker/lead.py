# @Time    : 2022-03-12 1:55 a.m.
# @Author  : Xiaoxia Li
# @FileName: test.py
# @Software: PyCharm
class Lead:

    def stimulate(self):
        pass

    def add_lead_pace(self):
        pass

    def get_chamber(self):
        pass

    # get info from heart/input
    def get_chamber(self):
        pass

    # Receive information from header
    # 起搏脉冲的波形是一个顶部略有下降的方波（如图2．11）。其幅度是指脉冲电压的最大值，一般取5V；其宽度是指脉冲的持续时间，多在0．5～1ms
    def header_info(self):

        pass

    # stimulate
    def stimulate(self):
        pass

    # pacing_therapy
    # cardiac depolarization
    #  sense every heartbeat (no under sensing)
    #  count it only once (no oversensing)

    # atrial output pulse
    def atrial_Output(self):
        pass

    # ventricular output pulse
    def ventricular_Output(self):
        pass

    # Sensing atrial via P wave
    # 固定频率的短阵快速起搏、递增（或递减）频率的短阵快速起搏、50Hz高频短阵起搏（0．5～3s）等
    def atrial_Sensing(self, P_waves, AtrialAmplitude):
            if AtrialAmplitude is None:
                print("%s None P wave")
                return
            elif AtrialAmplitude < 0.2:
                print("%s P wave is normal")
                return P_waves == True, AtrialAmplitude
            else:
                print("%s P wave is abnormal")
                return P_waves == False, AtrialAmplitude

    # Sensing ventricular via QRS
    def ventricular_Sensing(self):

        pass

    # Sensing both A and V
    def av_Sensing(self, P_waves, QRS_waves):
        self.atrial_Sensing(P_waves)
        self.ventricular_Sensing(QRS_waves)
        pass

    # pacing atrial
    def atrial_Pacing(self):
        pass

    # pacing ventricular
    def ventricular_Pacing(self):
        pass

    # pacing both A and V
    def av_Pacing(self):
        self.atrial_Pacing()
        self.ventricular_Pacing()
        pass

    # Inhibit response
    def inhibit_Response(self):
        pass

    # Trigger response
    def trigger_Response(self):
        pass

    # pacing both A and V
    def it_Response(self):
        self.inhibit_Response(self)
        self.trigger_Response(self)
        pass

    #  Standard Four-Letter Pacemaker Code
    # I chamber Paced AVDO
    def get_chamberPaced(self,chamber):
        if chamber == "Atrial":
            return self.atrial_Pacing(self)
        elif chamber == "Ventricular":
            return self.ventricular_Pacing()
        elif chamber == "Both":
            return self.av_Pacing()
        else:
            return "None"

    # II chamber Sensed AVDO
    # input heart beat
    # output hear beat
    def get_chamberSensed(self, chamber):
        if chamber == "Atrial":
            return self.atrial_Sensing(self)
        elif chamber == "Ventricular":
            return self.ventricular_Sensing(self)
        elif chamber == "Both":
            return self.av_Sensing(self)
        else:
            return "None"

    # III chamber Sensing Response ITDO
    def get_chamberResponse(self, mode):
        if mode == "Inhibit":
            return self.inhibit_Response()
        elif mode == "trigger":
            return self.trigger_Response()
        elif mode == "ITBoth":
            return self.it_Response()
        else:
            return "None"

    # IV rate modulation
    def rate_modulation(self):
        pass

    # discharge pulse
    def dishcarge_pulse(self):
        pass


def main():
    print(Lead.atrial_Sensing(Lead, True, 0.09))


if __name__  == '__main__':
    main()