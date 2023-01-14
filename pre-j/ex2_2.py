n = int(input())
day = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
for i in range (0,7):
    if n % 7 == i:
        print(day[i])
    i+=1