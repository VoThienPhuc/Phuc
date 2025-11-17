try:
    Tuoi = int(input("Nhập độ tuổi của bạn "))
    if Tuoi >= 18:
        print("Bạn đã đủ tuổi bầu cử")
    else:
        print("Bạn chưa đủ tuổi bầu cử")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")