def tinh_gia_tri_S():
    print ("Chương trình tính giá trị S")
    n = int(input("Nhập n (n>2): "))
    while True:
        try:
         if n>=2:
            break
         else:
            print("Vui lòng nhập lại n>= 2")
        except ValueError:
            print("Giá trị nhập vào không hợp lệ, vui lòng nhập lại.")
    TS = 0
    for i in range (1,n+1):
        TS += i
    MS = 0
    for i in range (2, n+1 , 2):
        MS += i
    S = TS / MS
    print (f"Giá trị S là: {S:.2f}")
tinh_gia_tri_S()