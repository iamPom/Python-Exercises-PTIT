# Bài 7.13 - B19DCCN507 Hoàng Hữu Phước
def build_profile(ten, *thong_tin_them):
    thongtin = {'Ten': ten}
    for i in thong_tin_them:
        thongtin.update(i)
    return thongtin


user_profile = build_profile('Hoang Huu Phuoc', {'Nghe Nghiep': 'Sinh vien'}, {'Gioi tinh': 'Nam'},
                             {'Tinh trang': 'Doc than'}, {'Gioi tinh': 'Nam'})
print(user_profile)
