import calendar
def bai_9():
    year = int(input("Nhập năm: "))
    month = int(input("Nhập tháng: "))
    print("\n----------------")
    print(calendar.month(year, month))
    print("----------------")
bai_9()