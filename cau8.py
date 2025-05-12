#Ham kt so nhi phan chia het cho 5 ko
def chia_het_cho_5(so_nhi_phan):
    #chuyen so nhi phan sang so thap phan
    so_thap_phan = int(so_nhi_phan, 2)
    #kt so thap phan chia het cho 5 ko
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
#nhap chuoi
chuoi_so_nhi_phan = input("Nhap chuoi so nhi phan (phan tach boi dau phay):")
#tach chuoi va kt
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5 (so) ]
if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Cac so nhi phna chia het cho 5 la:", ket_qua)
else:
    print("Khong co so nhi phan nao chia het cho 5trong chuoi da nhap.")