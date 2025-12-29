def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập N: "))
ds = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i + 1}: "))
    ds.append(so)
ds_nguyen_to = []
for x in ds:
    if is_prime(x):
        ds_nguyen_to.append(str(x))
chuoi = ", ".join(ds_nguyen_to)
so_luong = len(ds_nguyen_to)
print(f"Các số nguyên tố: {chuoi} (số lượng: {so_luong})")