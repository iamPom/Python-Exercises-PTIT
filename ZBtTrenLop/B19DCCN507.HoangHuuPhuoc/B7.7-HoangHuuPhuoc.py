# Bài 7.7 - B19DCCN507 Hoàng Hữu Phước
def make_album(ca_si, ten_album, soluong=None):
    album_dict = {'artist': ca_si, 'ten_album': ten_album}
    if soluong:
        album_dict['bai_hat'] = soluong
    return album_dict


print("album 1: ", make_album('Thu Phuong', 'Ha Noi va Toi'))
print("album 2: ", make_album('Do Bao', 'Canh cung', soluong=4))
print("album 2: ", make_album('Nguyen Tran Trung Quan', 'Khoi Hanh', soluong=7))