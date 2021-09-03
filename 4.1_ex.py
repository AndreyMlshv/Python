from sys import argv


def wages_calc(a, b, c):
    print((a * b) + c)


free_val, work_hours, rate, prize = argv
wages_calc(int(work_hours), int(rate), int(prize))

