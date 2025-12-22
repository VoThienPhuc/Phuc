import math
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range (2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def bai_6():
    n = int(input("Nhập số n: "))
    print(f"Các số nguyên tố nhỏ hơn {n} là: ")
    for i in range(2, n):
        if la_so_nguyen_to(i):
            print(i, end=", ")
    print()
bai_6()