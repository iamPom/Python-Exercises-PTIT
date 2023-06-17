# #Bai1
def TinhTuoi (nam_sinh):
    return 2021 - nam_sinh;

# #Bai2
# def DemTu(ho_ten):
#     return len(ho_ten.split(" "))

#Bai3
class Sinhvien:
    ho_ten, gioi_tinh, que_quan = "", "", ""
    nam_sinh = 0
    diem_toan, diem_ly, diem_hoa = 0, 0, 0
    diem_TB = 0
    diem_XT = 0

print("Nhap 10 sinh vien : ")
ds_SV = []

for i in range(2):
    print("Nhap sinh vien thu", (i+1), ":")
    sv = Sinhvien()
    sv.ho_ten = input("Nhap ho ten: ")
    sv.nam_sinh = int(input("Nhap nam sinh : "))
    # sv.gioi_tinh = input("Nhap gioi tinh : ")
    # sv.que_quan = input("Nhap que quan : ")
    # sv.diem_toan = float(input("Nhap diem toan : "))
    # sv.diem_ly = float(input("Nhap diem ly : "))
    # sv.diem_hoa = float(input("Nhap diem hoa : "))
    #
    # sv.diem_TB = float((sv.diem_toan + sv.diem_ly + sv.diem_hoa)/float(3))
    # sv.diem_XT = float(float(sv.diem_toan*2) + sv.diem_ly + sv.diem_hoa)

    ds_SV.append(sv)

print("Danh sach sinh vien va tuoi!!!!")
for i in ds_SV:
    print(f"{i.ho_ten}: {TinhTuoi(sv.nam_sinh)}")

# print("-" * 40)
#
# print("Danh sach sinh vien va diem TB")
# ds_SV.sort(key=lambda sv : sv.diem_TB)
# for i in ds_SV:
#     print(f"{i.ho_ten}: {round(i.diem_TB, 2)}")
# print("-"*40)
#
#
# print("So luong sinh vien nam va nu")
# count_nam = 0
# count_nu = 0
#
# for i in ds_SV:
#     if i.gioi_tinh == "Nam":
#         count_nam += 1
#     else: count_nu += 1
#
# print(f"Nam: {count_nam}, Nu: {count_nu}")
# print("-"*40)
#
# print("Danh sach sinh vien va so tu trong ten!!!!")
# for i in ds_SV:
#     print(f"{i.ho_ten}: {DemTu(sv.ho_ten)}")
# print("-"*40)
#
# print("Danh sach sinh vien va diem xet tuyen ")
# ds_SV.sort(key=lambda sv : sv.diem_XT, reverse=True)
# for i in ds_SV:
#     print(f"{i.ho_ten}: {round(i.diem_XT, 0)}")
# print("-"*40)