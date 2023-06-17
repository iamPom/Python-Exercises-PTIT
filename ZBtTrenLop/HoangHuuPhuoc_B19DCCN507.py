"""
Họ tên: Hoàng Hữu Phước
Mã Sinh viên: B19DCCN507
Email: phuoc20102001@gmail.com
Số điện thoại: 0337589366
"""


class FullName_HaNoi:
    def __init__(self, que_quan):
        self.que_quan = que_quan

    def getQue_quan(self):
        return self.que_quan

    # hàm sinh mã tỉnh
    def sinh_ma_tinh_B19DCCN507(self, ten_tinh, ma_tinh):
        for key, val in ma_tinh.items():
            if val == ten_tinh:
                return key
        return "-1"


class CongDan_HoangHuuPhuoc(FullName_HaNoi):
    def __init__(self, ho_ten, nam_sinh, gioi_tinh, que_quan):
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        FullName_HaNoi.__init__(self,que_quan)

    #lấy tên
    def getHo_ten(self):
        return self.ho_ten
    #lấy năm sinh
    def getNam_sinh(self):
        return self.nam_sinh
    #lấy giới tính
    def getGioi_tinh(self):
        return self.gioi_tinh
    # tính tuổi
    def tinh_tuoi_B19DCCN507(self, nam_sinh):
        return 2021 - nam_sinh;

    #Sinh mã giới tính
    def sinh_ma_gioi_tinh_B19DCCN507(self, nam_sinh, gioi_tinh):
        if nam_sinh >= 1900 and nam_sinh <= 1999:
            if gioi_tinh == "Nam":
                return 0
            else:
                return 1
        if nam_sinh >= 2000 and nam_sinh <= 2999:
            if gioi_tinh == "Nam":
                return 2
            else:
                return 3
        if nam_sinh >= 2100 and nam_sinh <= 2199:
            if gioi_tinh == "Nam":
                return 4
            else:
                return 5
        if nam_sinh >= 2200 and nam_sinh <= 2299:
            if gioi_tinh == "Nam":
                return 6
            else:
                return 7
        if nam_sinh >= 2300 and nam_sinh <= 2399:
            if gioi_tinh == "Nam":
                return 8
            else:
                return 9
        return -1

    def sinh_email_B19DCCN507(self, ho_ten):
        name = ho_ten.split()
        str = name[len(name) - 1]
        for i in range(len(name) - 1):
            str += name[i][0]
        return str + "@gmail.com"


ma_tinh = {"001": "Hà Nội", "002": "Hà Giang", "004": "Cao Bằng", "006": "Bắc Cạn", "008": "Tuyên Quang",
           "010": "Lào Cai", "011": "Điện Biên", "012": "Lai Châu", "014": "Sơn La", "015": "Yên Bái"}

cong_dan1 = CongDan_HoangHuuPhuoc("Hoàng Hữu Phước", 2001, "Nam", "Hà Nội")
cong_dan2 = CongDan_HoangHuuPhuoc("Hoàng Văn Nam", 2001, "Nam", "Lai Châu")
cong_dan3 = CongDan_HoangHuuPhuoc("Hoàng Trường Giang", 2001, "Nam", "Lào Cai")
cong_dan4 = CongDan_HoangHuuPhuoc("Nguyễn Văn Bắc", 2001, "Nam", "Lào Cai")
cong_dan5 = CongDan_HoangHuuPhuoc("Nguyễn Văn Trung", 2001, "Nam", "Yên Bái")
cong_dan6 = CongDan_HoangHuuPhuoc("Hoàng Trường Giang", 2001, "Nam", "Lào Cai")
cong_dan7 = CongDan_HoangHuuPhuoc("Hoàng Trường Giang", 2001, "Nam", "Lào Cai")
cong_dan8 = CongDan_HoangHuuPhuoc("Hoàng Trường Giang", 2001, "Nam", "Lào Cai")
cong_dan9 = CongDan_HoangHuuPhuoc("Hoàng Trường Giang", 2001, "Nam", "Lào Cai")
cong_dan10 = CongDan_HoangHuuPhuoc("Hoàng Hữu Phước", 2001, "Nam", "Hà Nội")

listCD = [cong_dan1, cong_dan2, cong_dan3, cong_dan4, cong_dan5, cong_dan6, cong_dan7, cong_dan8, cong_dan9, cong_dan10]

for i in listCD:
    print(i.getHo_ten(), i.getGioi_tinh(), i.tinh_tuoi_B19DCCN507(i.getNam_sinh()), i.getQue_quan(), i.sinh_email_B19DCCN507(i.getHo_ten()))