import math 
n = int(input("Nhập số n: "))
x = int(input("Nhập số x: "))
S = 0
for i in range(1 ,n + 1):
    S = math.sqrt(x + S)
print(f"S = {S:.3f}")
s2 = 0
for i in range(2 , n):
    s2 += x**i / i + 1
print(f"S2 = {s2:.3f}")
