def Clock(h, m):
    minutes = m + h * 60
    hours = round(minutes/60,0) % 24
    minutes = minutes % 60
    return "%02d:%02d" % (hours, minutes)