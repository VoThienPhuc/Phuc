def bai_10():
    m = input("Nhập số tự nhiên M: " )
    n = len(m)
    Tong = 0
    for chu_so in m:
        Tong += int(chu_so) ** n
    so_goc = int(m)
    if Tong == so_goc:
        print(f"{so_goc} là số Armstrong")
    else:
        print(f"{so_goc} không phải là số Armstrong")
bai_10()