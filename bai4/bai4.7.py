print("ho va ten:tran nhat anh")
print("Mssv:245752021610069")
chuoi = input("Nhập chuỗi: ")
chuoi_moi = ""
for ch in chuoi:
    if not ch.isdigit():
        chuoi_moi += ch

print("Chuỗi sau khi loại bỏ chữ số:", chuoi_moi)
