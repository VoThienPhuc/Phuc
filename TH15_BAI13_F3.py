i = int(input("Nhập vào một số tự nhiên: ")) 
Tongso = 0
for j in range(1, i + 1):
    Tongso += j
if i % 2 == 0 and i % 3== 0:
    print(f"Tổng các số từ 1 đến {i} là {Tongso}, số {i} vừa chia hết cho 2 và 3")
    