#Đêm số lương phần tử có giá trị chẵn và in ra màn hình
n = int(input("Nhập vào số phần tử của danh sách: "))
dem_chan = 0
for i in range(n):  
    so = int(input(f"Nhập phần tử thứ {i + 1}: "))
    if so % 2 == 0:
        dem_chan += 1
print(f"Số lượng phần tử có giá trị chẵn là: {dem_chan}")