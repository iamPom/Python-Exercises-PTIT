# Hoàng Hữu Phước - B19DCCN507 - 20/10/2001
# email: phuoc20102001@gmail.com
# sđt: 0337589366

from datetime import *

# remove dấu chữ cái tiếng Việt (cho phần email)
import re


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


def get_months_B19DCCN507(stringBirthDay):
    tachngay = stringBirthDay.split('/')
    return tachngay[1]


def get_used_months_Thai(string):
    hientai = datetime.now().date()
    s = string.split('/')
    time = date(year=int(s[2]), month=int(s[1]), day=int(s[0]))
    use_month = (hientai - time).days // 30
    return use_month


def B19DCCN507_get_used_months(stringName, stringBirthDay):
    listname = stringName.split()
    username = ''
    listngaysinh = stringBirthDay.split('/')
    username += no_accent_vietnamese(listname[len(listname)-1]) + listngaysinh[0]+listngaysinh[1]
    return username.lower()


class KhachHang_B19DCCN507:
    def __init__(self, makh, tenkh, birthday, dvu):
        self.makh = makh
        self.tenkh = tenkh
        self.username = B19DCCN507_get_used_months(tenkh, birthday)
        self.birthday = birthday
        self.dvu = dvu.dvu
        self.ngaydangki = dvu.ngaydangki
        self.loaigoi = dvu.loaigoi
        self.gia= dvu.gia
        


class DichVu_B19DCCN507:
    def __init__(self, maDV, ngaydangki):
        self.maDV = maDV
        if maDV == '001':
            self.loaigoi = 'Đồng'
            self.gia = '500.000đ/tháng'
        elif maDV == '002':
            self.loaigoi = 'Bạc'
            self.gia = '1.000.000đ/tháng'
        elif maDV == '003':
            self.loaigoi = 'Vàng'
            self.gia = '2.000.000đ/tháng'
        elif maDV == '002':
            self.loaigoi = 'Kim Cương'
            self.gia = '3.000.000đ/tháng'
        self.ngaydangki = ngaydangki


print(B19DCCN507_get_used_months('Hoang Huu Phước', '20/10/2001'))
# print(get_used_months_Thai('05/06/2020'))
# print(get_months_B19DCCN507('20/10/2001'))
