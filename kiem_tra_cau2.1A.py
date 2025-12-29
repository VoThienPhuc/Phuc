n = int(input("Nhập n: "))
S = 0
for i in range(1, 2 * (n + 1), 2):
    S += i
print(f"Tổng S = {S}")