von = 100000000
lai_suat = 0.07
nam = 10
print (f"Đầu tư {von:,.0f} VND với lãi suất kép {lai_suat*100}% trong {nam} năm")
for i in range (1, nam + 1):
    von = von * (1 + lai_suat)
    print(f"Năm {i}: {von:,.0f} VND ")
print (f"Tổng số tiền sau {nam} năm là {von:,.0f} VND")