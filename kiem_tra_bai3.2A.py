n = int(input("Nhập N: "))
so_chan = 0
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i + 1}: "))
    if i % 2 == 0:
        so_chan += so
print(f"Tổng các phần tử ở vị trí chẵn là: {so_chan}")