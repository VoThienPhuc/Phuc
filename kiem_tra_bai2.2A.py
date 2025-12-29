n = int(input("Nhập n: "))
S3 = 0
for i in range(1, n + 1):
    S3 += 1 / (i * (i + 1))
print(f"Tổng S3 = {S3:.3f}")