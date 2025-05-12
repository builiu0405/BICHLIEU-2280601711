#Nhap so
so = int(input("Nhap mot so nguyen:"))
#KT so chan ko
if so % 2 == 0:
    print(so, "la so chan.")
else:
    print(so, "khong phai la so chan.")