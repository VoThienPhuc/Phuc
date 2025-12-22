def so_lon_nhat(a, b, c):
    so_lon_nhat = a
    if b > so_lon_nhat:
        so_lon_nhat = b
    if c > so_lon_nhat:
        so_lon_nhat = c
    return so_lon_nhat
def so_nho_nhat(a, b, c):
    so_nho_nhat = a
    if b < so_nho_nhat:
        so_nho_nhat = b
    if c < so_nho_nhat:
        so_nho_nhat = c
    return so_nho_nhat
def max_min():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    c = int(input("Nhập c: "))
    print(f"Số lớn nhất là: {so_lon_nhat(a, b, c)}")
    print(f"Số nhỏ nhất là: {so_nho_nhat(a, b, c)}")
max_min()