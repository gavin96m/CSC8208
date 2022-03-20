# @Time    : 2022-03-12 1:55 a.m.
# @Author  : Xiaoxia Li
# @FileName: test.py
# @Software: PyCharm
# Description: a basic class for lead object
from pacemaker.heart import Heart


class HeartConfig(object):

    # define chamber a
    @staticmethod
    def transit_chamber_a(self):
        return Heart.atrial

    # define chamber b
    @staticmethod
    def transit_chamber_v(self):
        return Heart.ventricular

    # transit p value
    def transit_p(self):
        p = self.heart_arr()[0]
        return p

    # transit q value
    def transit_qrs(self):
        q = self.heart_arr()[2]
        return q

    # calculate rr interval
    def cal_rr(self):
        arr = self.heart_arr()
        rr_time = 1 / 2 * arr[3] + arr[5] + arr[6] + arr[8] + 1 / 2 * arr[10]
        return rr_time

    # calculate pp interval
    def cal_pp(self):
        arr = self.heart_arr()
        pp_time = 1 / 2 * arr[1] + arr[3] + arr[5] + arr[6] + 1 / 2 * arr[8]
        return pp_time

    # read heart information from file
    @staticmethod
    def heart_arr(self):
        print("file")
        # with open()
        with open("../heart_output.txt", "r") as f:
            heart_file = []
        print("read")
        for line in f.readlines():
            cur_line = line.strip().split(",")
            heart_file.append(cur_line[:])
        print(heart_file)
        return heart_file


def main():
    #    arr=[ p_amplitude,  pq_time, qrs_height, qrs_time,st_level,st_time,sleep]
    #    arr= [0.15, 160, 1.5, 100, 0, 150,sleep, 0.15, 160, 1.5, 100, 0, 150]
    # arr = [0.15, 200, 1.5, 120, 0, 150, 530, 0.15, 200, 1.5, 120, 0, 150]  # lower limit 60
    # arr = [0.05, 400, 0.8, 250, 0, 150, 530, 0.05, 400, 0.8, 250, 0, 150]  # slow 45
    # arr = [0.15, 120, 1.5, 80, 0, 150, 250, 0.15, 120, 1.5, 80, 0, 150]  # upper limit 60
    arr = [0.25, 60, 3.5, 40, 0, 150, 250, 0.25, 60, 3.5, 40, 0, 150]  # faster 120
    print(1 / 2 * arr[3], arr[5], arr[6], arr[8], 1 / 2 * arr[10])  # rr
    print(1 / 2 * arr[1], arr[3], arr[5], arr[6], 1 / 2 * arr[8])  # pp
    t1 = HeartConfig.cal_rr(arr)
    t2 = HeartConfig.cal_pp(arr)
    print(t1, t2)
    print(60000 / t1)
    HeartConfig.heart_arr()


if __name__ == '__main__':
    main()
