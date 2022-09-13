def make_readable(seconds):
    a,sec = divmod(seconds, 60)
    hour, min = divmod(a, 60)
    return f'{str(hour).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}'

def make_readable_best(seconds):
    a,sec = divmod(seconds, 60)
    hour, min = divmod(a, 60)
    return '{:02}:{:02}:{:02}'.format(hour, min, sec)

print(make_readable_best(399))