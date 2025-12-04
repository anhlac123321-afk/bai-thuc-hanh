print("ho va ten:tran nhat anh")
print("Mssv:245752021610069")
n = int(input("Nhập n: "))

triangle = []

for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

for row in triangle:
    print(row)
