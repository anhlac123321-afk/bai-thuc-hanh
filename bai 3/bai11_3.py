def benefit(t, n, k):
    for _ in range(k):
        n += n * (t / 100)
    return n

t = float(input("Nhập lãi suất (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

so_tien_nhan_duoc = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {so_tien_nhan_duoc:.2f}")
