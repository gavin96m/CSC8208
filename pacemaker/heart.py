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


class HeartConfig(object):

    # define chamber a
    @staticmethod
    def transit_chamber_a():
        return "Atrial"

    # define chamber b
    @staticmethod
    def transit_chamber_v():
        return "Ventricular"

    # transit p value
    def transit_p(self, i):
        return self.heart_arr()[i][0]

    # transit q value
    def transit_qrs(self, i):
        return self.heart_arr()[i][2]

    # transit pr interval
    def transit_pr(self, i):
        return self.heart_arr()[[i]][0]/2

    # calculate rr interval
    def cal_rr(self, i):
        arr = self.heart_arr()[i]
        print(arr)
        rr_time = 1 / 2 * arr[3] + arr[5] + arr[6] + arr[8] + 1 / 2 * arr[10]
        print(rr_time)
        return rr_time

    # calculate pp interval
    def cal_pp(self, i):
        arr = self.heart_arr()[i]
        pp_time = 1 / 2 * arr[1] + arr[3] + arr[5] + arr[6] + 1 / 2 * arr[8]
        return pp_time

    # read heart information from file
    @staticmethod
    def heart_arr():
        # with open()
        with open("Pacemaker-CSC8208/heart_info", "r") as f:
            heart_file = []
            for line in f.readlines():
                cur_line = line.strip().split(", ")
                for idx, val in enumerate(cur_line):
                    cur_line[idx] = float(val)
                heart_file.append(cur_line[:])
        return heart_file

def main():
    print(HeartConfig.heart_arr())
    # print(HeartConfig.transit_chamber_a())
    # arr=[ p_amplitude,  pq_time, qrs_height, qrs_time,st_level,st_time,sleep]
    # arr = [0.15, 200, 1.5, 120, 0, 150, 530, 0.15, 200, 1.5, 120, 0, 150]  # lower limit 60
    # arr = [0.05, 400, 0.8, 250, 0, 150, 530, 0.05, 400, 0.8, 250, 0, 150]  # slow 45
    # arr = [0.15, 120, 1.5, 80, 0, 150, 250, 0.15, 120, 1.5, 80, 0, 150]  # upper limit 60
    # arr = [0.25, 60, 3.5, 40, 0, 150, 250, 0.25, 60, 3.5, 40, 0, 150]  # faster 120
    # print(1 / 2 * arr[3], arr[5], arr[6], arr[8], 1 / 2 * arr[10])  # rr
    # print(1 / 2 * arr[1], arr[3], arr[5], arr[6], 1 / 2 * arr[8])  # pp
    t1 = HeartConfig.cal_rr(HeartConfig, 0)
    t2 = HeartConfig.cal_pp(HeartConfig, 0)
    print(t1, t2)
    print(60000 / t1)


if __name__ == '__main__':
    main()