print("ho va ten:tran nhat anh")
print("Mssv:245752021610069")
n = int(input("Nhập n: "))

fib = [0, 1]
result = [0]

if n > 1:
    result.append(1)

while True:
    next_f = fib[-1] + fib[-2]
    if next_f >= n:
        break
    fib.append(next_f)
    result.append(next_f)

print(result)
