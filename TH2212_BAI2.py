def max_min():
 a = int(input("Nhập a: "))
 b = int(input("Nhập b: "))
 c = int(input("Nhập c: "))
 so_lon_nhat = a
 if b > so_lon_nhat:
        so_lon_nhat = b
 if c > so_lon_nhat:
        so_lon_nhat = c
 so_nho_nhat = a
 if b < so_nho_nhat:
        so_nho_nhat = b
 if c < so_nho_nhat:
        so_nho_nhat = c
 print(f"Số lớn nhất là: {so_lon_nhat}")
 print(f"Số nhỏ nhất là: {so_nho_nhat}")
max_min()
        