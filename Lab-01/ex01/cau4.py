#Tao mot danh sach rong 
j=[]
#Duyet tat ca cac so trong doan tu 2000 den 3200 , kt so i co chia het cho 7 va la boi so cua 5
for i in range (2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print (','.join(j))