# @Time    : 2022-03-10 12:26 p.m.
# @Author  : Xiaoxia Li
# @FileName: test.py
# @Software: PyCharm
# Description: a basic class for lead object

# fundamental class of heart
class Heart(object):

    def __init__(self, atrial, ventricular):
        self.atrial = atrial
        self.ventricular = ventricular

  # toString
    def __str__(self):
        return "%s: %s" % (self.atrial, self.ventricular)


def main():
    heart = Heart("Atrial", "Ventricular")
    print(heart.__str__())


if __name__ == '__main__':
    main()

# class to store heart data
class HeartData(object):

    def __init__(self, heart_rate, p_amplitude, qrs_height, st_level, t_amplitude,
                 p_time, pq_time, qrs_time, st_time, t_time):
        self.heart_rate = heart_rate
        self.p_amplitude = p_amplitude
        self.qrs_height = qrs_height
        self.st_level = st_level
        self.t_amplitude = t_amplitude
        self.p_time = p_time
        self.pq_time = pq_time
        self.qrs_time = qrs_time
        self.st_time = st_time
        self.t_time = t_time

  # toString
    def __str__(self):
        return "%s: %s  %s  %s  %s  %s  %s  %s  %s  %s" % \
               (self.heart_rate, self.p_amplitude,  self.qrs_height,
                self.st_level, self.t_amplitude, self.p_time, self.pq_time,
                self.qrs_time,  self.st_time, self.t_time)


def main():
    heart = HeartData(90,0.15, 1.5, 0, 0.30, 110, 160, 100, 150, 150)
    print(heart.__str__())


if __name__ == '__main__':
    main()