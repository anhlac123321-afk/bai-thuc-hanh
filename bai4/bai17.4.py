print("ho va ten:tran nhat anh")
print("Mssv:245752021610069")
n = int(input("Nhập n: "))
for i in range(1, n):
    tong = sum(j for j in range(1, i) if i % j == 0)
    if tong > i:
        print(i, end=" ")
