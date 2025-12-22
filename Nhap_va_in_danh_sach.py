n = int(input("Nhập số lượng phần tử n:"))
list = []
for i in range(n):
    Val = int(input(f"Nhập phần tử thứ {i+1}:"))
    list.append(Val)
print("Danh sách các phần tử đã nhập là:", list)