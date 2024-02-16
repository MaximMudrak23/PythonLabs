import math

x = int(input("X: ")) 
a = int(input("Y: "))
eps = float(input("Eps: "))
sum = 0
sum_current = 0
k = 0

while(True):
    ak = (math.sin(pow(a, k)) + math.cos(pow(a, k))) / math.factorial((k * k))
    sum_current += ak
    if(math.fabs(sum_current - sum) < eps):
        break
    sum += ak
    k += 1

print(sum_current)
print(k)