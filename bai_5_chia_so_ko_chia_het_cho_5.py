def bai_5():
    while True:
        n = int(input("Nhấp n ( n<=0 n <= 1000): "))
        if 0 < n <= 1000:
            break
        print ("Vui lòng nhập lại n!")
    print("Các sô không chưa hết cho 5 là: ")
    for i in range(1 , n + 1):
        if i % 5 != 0:
            print(i , end = ", ")
    print()
bai_5()