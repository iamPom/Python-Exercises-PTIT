#Nguyễn Thị Thái - B19DCCN639
# email: thaimeowmeow1510@gmail.com
# sdt : 0582745442
from datetime import *
def get_months_B19DCCN639(stringBirthDay):
    s = stringBirthDay.split('/')
    return s[1]

def get_used_months_Thai(string):
    hientai = datetime.now().date()
    s = string.split('/')
    time = date(year= int(s[2]),month=int(s[1]),day=int(s[0]) )
    use_month = (hientai - time).days // 30
    return use_month

def B19DCCN639_get_username(stringName,stringBirthday):
    a = stringName.split(" ")
    email = ""
    email += a[len(a) - 1]
    for i in range(0, len(a) - 1):
        email += a[i][0]
    day = stringBirthday.split("/")
    email += day[0] + day[1]
    return email.lower()
#print(B19DCCN639_get_username('Nguyễn Văn Minh','20/11/1990'))

class KhachHang_B19DCCN639:
    def __init__(self,stt,ten,birthday,DV):
        self.maKH = 'KH' + str(stt)
        self.ten = ten
        self.birthday = birthday
        self.username = B19DCCN639_get_username(self.ten,self.birthday)
        self.maDV = DV.ma
        self.ngayDK = DV.ngayDK
        self.goiDV = DV.goi
        self.giaDV = DV.gia


class DichVu_B19DCCN639:
    def __init__(self,ma,ngayDK):
        self.ma = ma
        if ma == '001':
            self.goi = 'Đồng'
            self.gia = '500.000đ/tháng'
        elif ma == '002':
            self.goi = 'Bạc'
            self.gia = '1.000.000đ/tháng'
        elif ma == '003':
            self.goi = 'Vàng'
            self.gia = '2.000.000đ/tháng'
        elif ma == '004':
            self.goi = 'Kim cương'
            self.gia = '3.000.000đ/tháng'
        self.ngayDK = ngayDK
print('Câu a :')
list = []

list.append(KhachHang_B19DCCN639(1,'Nguyen Thi Thai','15/10/2001',DichVu_B19DCCN639('001','15/11/2021')))
list.append(KhachHang_B19DCCN639(2,'Nguyen Thi Thu','21/09/2001',DichVu_B19DCCN639('003','15/07/2021')))
list.append(KhachHang_B19DCCN639(3,'Tran Thai Linh','09/08/1999',DichVu_B19DCCN639('004','10/10/2019')))
list.append(KhachHang_B19DCCN639(4,'Tran Huyen Trang','12/12/2000',DichVu_B19DCCN639('001','15/08/2021')))
list.append(KhachHang_B19DCCN639(5,'Nguyen Hai Duong','15/10/2005',DichVu_B19DCCN639('002','12/03/2016')))
list.append(KhachHang_B19DCCN639(6,'Nguyen Thi Thom','15/09/2001',DichVu_B19DCCN639('001','15/11/2021')))

print('Câu b :')
for i in list :
    if get_months_B19DCCN639(i.birthday) == '09':
        print(i.ten +'          ' +i.username +'            '+i.goiDV)
print('Câu c:')
for i in list :
    if get_used_months_Thai(i.ngayDK) > 12:
        print(i.ten +'          ' +i.goiDV +'            '+str(get_used_months_Thai(i.ngayDK)))

print('Câu d:')
import matplotlib.pyplot as plt
def DoanhThu(KH):
    return get_used_months_Thai(KH.ngayDK) * KH.giaDV
hang_x,hang_y = [],[]
for i in list :
    hang_x.append(i.maKH)
    hang_y.append(DoanhThu(i))

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(hang_x,hang_y)
ax.set_title("Doanh Thu cua DV", fontsize=24)
ax.set_xlabel("MaKH", fontsize=14)
ax.set_ylabel("Doanh Thu", fontsize=14)
# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)
plt.show()