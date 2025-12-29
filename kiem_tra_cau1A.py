a = float(input("Nhập vào điểm trung bình của học sinh: "))
if a >= 8  :
    print("Học sinh giỏi")
elif a >= 6.5 and a < 8:
    print("Học sinh khá")
elif a >= 5 and a < 6.5:
    print("Học sinh trung bình")
elif a >= 3.5 and a < 5:
    print("Học sinh yếu")
elif a < 3.5:
    print("Học sinh kém")
else:
    print("Điểm không hợp lệ")