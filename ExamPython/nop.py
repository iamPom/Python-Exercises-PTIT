# Hoàng Hữu Phước - B19DCCN507 - 20/10/2001
# email: phuoc20102001@gmail.com
# sđt: 0337589366


import random

sv_names=['lê MINH Hiếu',' Hoàng anh TÙng','Nguyễn Trần Yến ', 'Lê CÔNG VINh ', 'Mai Tiến Dũng ',' TRẦN MinH ', 'Nguyễn NAM ANH', 'LÊ Vĩnh phúc', 'Lê Hoàng MINH']
quequan=['Hải Dương','Hà Nội','Vĩnh Phúc','Hòa Bình', 'Sơn La', 'NamĐịnh','Ninh Bình','Hà Giang','Thanh Hóa','Nghệ An', 'Quảng Ninh']
so_thich=['Bóng đá','Cầu lông','Games','Xe đạp','Truyện tranh','Nhiếpảnh','Du lịch','Đọc sách','Chơi cờ','Cắm trại']
def chuan_hoa_ten_B19DCCN507(ten):
    xauChuanHoa = ten.lower().strip().split()
    xau = ''
    for i in xauChuanHoa:
        xau += i.title() + ' '
    return xau


def chon_ngau_nhien_HoangHuuPhuoc(danhsach, so):
    list_copy = danhsach[:]
    list_random = []
    for i in range(so):
        cdx = random.choice(list_copy)
        list_random.append(cdx)
        list_copy.remove(cdx)
    return list_random


def diem_TB_B19DCCN507(dict):
    diemTb=0
    diemTb += dict.get('cc') * 0.1 + dict.get('tbkt') * 0.1 + dict.get('btl') * 0.2 + dict.get('thi') * 0.6
    return format(diemTb, '.2f')



# chạy thử các hàm
# chuẩn hóa tên
print('\nHọ tên: ', chuan_hoa_ten_B19DCCN507('HOÀng    hữU  PhƯỚC'))
# ngau nhien
listtest = [1, 2, 3, 4, 5, 6, 7]
print('list ngau nhien:', chon_ngau_nhien_HoangHuuPhuoc(listtest, 4))
print()

Dict = [{'ma sv': 1,'ten sv':chuan_hoa_ten_B19DCCN507(chon_ngau_nhien_HoangHuuPhuoc(sv_names,1)[0]),'diem TP':{'cc': random.choice(1,10),'tbkt':random.choice(1,10),'btl':random.choice(1,10),'thi':random.choice(1,10)},
         'noi sinh':chon_ngau_nhien_HoangHuuPhuoc(quequan,1),'so thich': chon_ngau_nhien_HoangHuuPhuoc(so_thich,2)  },
{'ma sv': 2,'ten sv':chuan_hoa_ten_B19DCCN507(chon_ngau_nhien_HoangHuuPhuoc(sv_names,1)[0]),'diem TP':{'cc': random.choice(1,10),'tbkt':random.choice(1,10),'btl':random.choice(1,10),'thi':random.choice(1,10)},
         'noi sinh':chon_ngau_nhien_HoangHuuPhuoc(quequan,1),'so thich': chon_ngau_nhien_HoangHuuPhuoc(so_thich,3)  },
{'ma sv': 3,'ten sv':chuan_hoa_ten_B19DCCN507(chon_ngau_nhien_HoangHuuPhuoc(sv_names,1)[0]),'diem TP':{'cc': random.choice(1,10),'tbkt':random.choice(1,10),'btl':random.choice(1,10),'thi':random.choice(1,10)},
         'noi sinh':chon_ngau_nhien_HoangHuuPhuoc(quequan,1),'so thich': chon_ngau_nhien_HoangHuuPhuoc(so_thich,4)  },
{'ma sv': 4,'ten sv':chuan_hoa_ten_B19DCCN507(chon_ngau_nhien_HoangHuuPhuoc(sv_names,1)[0]),'diem TP':{'cc': random.choice(1,10),'tbkt':random.choice(1,10),'btl':random.choice(1,10),'thi':random.choice(1,10)},
         'noi sinh':chon_ngau_nhien_HoangHuuPhuoc(quequan,1),'so thich': chon_ngau_nhien_HoangHuuPhuoc(so_thich,1)  },
{'ma sv': 5,'ten sv':chuan_hoa_ten_B19DCCN507(chon_ngau_nhien_HoangHuuPhuoc(sv_names,1)[0]),'diem TP':{'cc': random.choice(1,10),'tbkt':random.choice(1,10),'btl':random.choice(1,10),'thi':random.choice(1,10)},
         'noi sinh':chon_ngau_nhien_HoangHuuPhuoc(quequan,1),'so thich': chon_ngau_nhien_HoangHuuPhuoc(so_thich,5)  },
{'ma sv': 6,'ten sv':chuan_hoa_ten_B19DCCN507(chon_ngau_nhien_HoangHuuPhuoc(sv_names,1)[0]),'diem TP':{'cc': random.choice(1,10),'tbkt':random.choice(1,10),'btl':random.choice(1,10),'thi':random.choice(1,10)},
         'noi sinh':chon_ngau_nhien_HoangHuuPhuoc(quequan,1),'so thich': chon_ngau_nhien_HoangHuuPhuoc(so_thich,2)  },
]

print("Câu b")

for i in Dict[:] :
    xau = ''
    xau += i['ma sv']+'       '+ i['ten sv'] + '        '+  diem_TB_B19DCCN507(i['diem tp'])+ '         ' +i['noi sinh'][0]+'       '
    for casy in i['so thich']:
        xau += str(casy)+', '

    print(xau)