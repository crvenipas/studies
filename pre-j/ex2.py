a = int(input())
b = int(input())
n = int(input())

a *= 60
sum_sec = a + b
n_sec = sum_sec * n

h = n_sec // 3600
m = (n_sec - h*3600) // 60
s = (n_sec - h*3600) - (m * 60)

print(h, m, s)