def tinh_chu_vi_dien_tich():
    print("tính chu vi và diện tích hình chữ nhật")
while True:
    try:
        w = float(input("Nhập chiều dài hình chữ nhật (0.0<= w <= 100.0) : "))
        h = float(input("Nhập chiều rộng hình chữ nhật (0.0<= h <= 100.0): "))
        if 0.0 <= w <= 100.0 and 0.0 <= h <= 100.0:
            break
        else:
            print("Giá trị nhập vào không hợp lệ, vui lòng nhập lại.")
    except ValueError:
        print("Giá trị nhập vào không hợp lệ, vui lòng nhập lại.")
chu_vi = 2 * (w + h)
dien_tich = w * h
print(f"Chu vi hình chữ nhật là: {chu_vi:.2f}")
print(f"Diện tích hình chữ nhật là: {dien_tich:.2f}")
tinh_chu_vi_dien_tich()