# Họ tên: Trần Xuân Độ
# mã SV: B19DCCN183
# Ngày sinh: 25/05/2001
# Sdt: 0825124160
import re
from datetime import *


def no_accent_vietnamese(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s


def get_year_B19DCCN183(ngaySinh):
    tmp = ngaySinh.split('/')
    return int(tmp[2])


def get_username_Do(hoTen, ngaySinh):
    # bỏ dấu tách chuỗi họ tên
    tmp1 = no_accent_vietnamese(hoTen.lower()).split(' ')
    tmp2 = ngaySinh.split('/')
    res = ''
    res += tmp1[-1]
    for i in range(0, len(tmp1)-1):
        res += tmp1[i][0]
    res += tmp2[2]
    return res


def get_minutes_B19DCCN183(ngayThangTruyCap):
    # s1s = ngayThangTruyCap[0:11].split("/")
    s2s = ngayThangTruyCap[11:18].split(":")
    tmp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # s1 = tmp[0:11].split("/")
    s2 = tmp[11:18].split(":")
    res = (int(s2[0])*3600+int(s2[1])*60+int(s2[2]))-(int(s2s[0])*3600+int(s2s[1])*60+int(s2s[2]))//60
    return res


class NguoiDung_B19DCCN183:
    def __init__(self, ma, ten, ngaySinh, thongTinTruyCap):
        self.ma = ma
        self.ten = ten
        self.ngaySinh = ngaySinh
        self.username = get_username_Do(self.ten, self.ngaySinh)
        self.thongTinTruyCap = thongTinTruyCap


class TruyCap_B19DCCN183:
    def __init__(self, loaiTruyCap, thoiDiemTruyCap):
        self.loaiTruyCap = loaiTruyCap
        self.thoiDiemTruyCap = thoiDiemTruyCap


# Câu a:
us1 = NguoiDung_B19DCCN183('U001', 'Trần Xuân Độ', '25/05/2002',
                           TruyCap_B19DCCN183('bình thường', '22/12/2021 05:21:13'))
us2 = NguoiDung_B19DCCN183('U002', 'Trần Thị Huyền Trang', '01/01/2001',
                           TruyCap_B19DCCN183('nguy cơ thấp', '22/02/2021 06:21:13'))
us3 = NguoiDung_B19DCCN183('U003', 'Trần Thị Huyền Anh', '25/04/2003',
                           TruyCap_B19DCCN183('nguy cơ cao', '22/12/2021 07:22:13'))
us4 = NguoiDung_B19DCCN183('U004', 'Trần Việt Tiệp', '06/09/2005',
                           TruyCap_B19DCCN183('tấn công', '10/12/2021 10:21:13'))
us5 = NguoiDung_B19DCCN183('U005', 'Trần Thị Thanh', '14/05/2001',
                           TruyCap_B19DCCN183('bình thường', '24/12/2021 05:21:13'))
# Câu b
ds = [us1, us2, us3, us4, us5]
ds2 = sorted(ds, key=lambda x: get_year_B19DCCN183(x.ngaySinh))
for i in ds2:
    tmp = i.ten+" "+i.username+" " + i.ngaySinh
    print(tmp)
# Câu c
for i in ds:
    if i.thongTinTruyCap.loaiTruyCap == 'nguy cơ cao':
        tmp = i.username+" "+str(get_minutes_B19DCCN183(i.thongTinTruyCap.thoiDiemTruyCap))+" "+ i.thongTinTruyCap.loaiTruyCap
        print(tmp)