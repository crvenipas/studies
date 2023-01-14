
time_mins = int(input())
start_hours = int(input())
start_mins = int(input())

spent_h = time_mins // 60
h = start_hours + spent_h
if h >= 24:
    h -= 24
m = time_mins - spent_h * 60 + start_mins
if m >= 60:
    m -= 60
    h += 1
print(h, m)