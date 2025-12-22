list = [ 5 , 12 , -3 , 8 , 20 , 7]
dem_chan =0 
for i in list:
    if i % 2 == 0:
        dem_chan += 1
print("Số lượng số chẵn trong danh sách là:", dem_chan)
dem_le = [i for i in list if i % 2 != 0]
print(f"Số lượng số lẻ trong danh sách là:", {len(dem_le)})
list.sort()
print("Danh sách tăng dần là:", list)
list.sort(reverse=True)
print("Danh sách giảm dần là:", list)