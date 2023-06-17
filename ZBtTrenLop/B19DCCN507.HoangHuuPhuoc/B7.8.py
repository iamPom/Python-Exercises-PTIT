# Bài 7.8 - B19DCCN507 Hoàng Hữu Phước
def make_album(ca_si, ten_album, soluong=None):
    album_dict = {'artist': ca_si, 'ten_album': ten_album}
    if soluong:
        album_dict['bai_hat'] = soluong
    return album_dict


t = int(input("nhap so album: "))
for i in range(t):
    ca_si = input("Ten ca si: ")
    ten_album = input("Ten album: ")
    soluong = int(input("So luong: "))
    print("album thu", i + 1, make_album(ca_si, ten_album, soluong))
