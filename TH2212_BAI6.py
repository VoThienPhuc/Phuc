n = int(input("Nhập danh sách n bài hát yêu thích:"))
list = []
for i in range(n + 1):
    TenBH = input(f"Nhập bài hát thứ {i+1}:")
    list.append(TenBH) 
print("Danh sách các bài hát yêu thích là:", list)       