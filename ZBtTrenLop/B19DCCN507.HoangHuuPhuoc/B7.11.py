# Bài 7.11- B19DCCN507 Hoàng Hữu Phước
def send_messages(ds_tin_nhan):
    sent_messages = []
    for i in ds_tin_nhan:
        print(i)
        sent_messages.append(i)
    print(ds_tin_nhan)
    print(sent_messages)


ds_tin_nhan = ["Cau dang lam gi the?", "To dang thuc hanh python", "Kho khong cau oi?", "Huhu kho cau a :(("]
ds_tin_nhan1 = ds_tin_nhan.copy()
send_messages(ds_tin_nhan1)
print("Danh sach messages dau va sau khi goi")
print(ds_tin_nhan)
print(ds_tin_nhan1)