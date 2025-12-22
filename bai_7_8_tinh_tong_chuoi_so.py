import math
def bai_7_8():
    n = int(input("Nhập số n: "))
    s_harmonic = 0
    for i in range(1, n + 1):
        s_harmonic += 1 / i
        print(f"Tổng Harmaonic = {s_harmonic}")
    s1 = 0
    for i in range(1,  + 1):
      s1 += 1 / (i * (i + 1))
    print(f"Tổng S1 = {s1}")
    s2 = 0   
    for i in range(n):
      s2 = math.sqrt(3 + s2)
    print(f"S1 = {s1:.3f}")
    print(f"S2 = {s2:.3f}")
bai_7_8()