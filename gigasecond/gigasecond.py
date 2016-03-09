import datetime

gs_per_s = 1000000000

def add_gigasecond(start):
    return start + datetime.timedelta(seconds = gs_per_s)