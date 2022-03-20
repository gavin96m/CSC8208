class Test(object):

    p_amplitude = 0
    qrs_height = 0
    st_level = 0
    t_amplitude = 0
    pr_time = 0
    qrs_time = 0
    st_time = 0

    def __init__(self, p_amplitude,  pr_time, qrs_height, qrs_time,st_level,st_time):
        self.p_amplitude = p_amplitude
        self.pr_time = pr_time
        self.qrs_height = qrs_height
        self.qrs_time = qrs_time
        self.st_level = st_level
        self.st_time = st_time

    # arr=[p_amplitude,  pr_time, qrs_height, qrs_time,st_level,st_time]

    def cal_rr(arr):
        rr_time = 1/2 * arr[3]+arr[5]+arr[7] + 1/2 * arr[9]
        return rr_time

    def cal_pp(arr):
        pp_time = 1/2 * arr[1]+arr[3]+arr[5] + 1/2 * arr[7]
        return pp_time

    def getData(self):
        return [self.p_amplitude,  self.pr_time, self.qrs_height, self.qrs_time,self.st_level,self.st_time]


def main():

        t1 = Test(0.15,  160, 1.5, 100,0,150)
        print(t1.getData())
        t2 = Test(0.15,  160, 1.5, 100,0,150)
        print(t2.getData())
        t3 = t1.getData()+t2.getData()
        print(t3)
        print(Test.cal_rr(t3))


if __name__ == '__main__':
        main()
