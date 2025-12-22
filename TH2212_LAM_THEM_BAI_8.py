def bai_them_bai_8():
    print("Chương trình in và tính tổng dãy số fibonacci")
    n = int(input("Nhập số phần tử của dãy Fibonacci: "))
    while   True:
        try:
         if n > 0:
            break
         print("Vui lòng nhập lại n!")
        except ValueError:
            print("Giá trị nhập vào không hợp lệ, vui lòng nhập lại.")
    ds_fibo = []
    if n == 1:
       dsfibo = [0]
    if n == 2:
       ds_fibo= [0, 1]
    else:
         ds_fibo = [0, 1]
         for i in range(2, n):
              next_fibo = ds_fibo[i-1] + ds_fibo[i-2]
              ds_fibo.append(next_fibo)
    print("Dãy Fibonacci:", ds_fibo)
    print("Tổng dãy Fibonacci:", sum(ds_fibo))
bai_them_bai_8()