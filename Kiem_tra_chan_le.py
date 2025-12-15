try:
    so = int(input("Nhập vào một số nguyên: "))
    if so % 2 == 0:
        print(f"Số {so} là số chẵn")
    else:
        print(f"Số {so} là số lẻ")
except ValueError:
    print("Vui lòng nhập vào một số nguyên hợp lệ.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")