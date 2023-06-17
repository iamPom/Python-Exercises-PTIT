# Bài 7.10 - B19DCCN507 Hoàng Hữu Phước
def send_messages(ds_tin_nhan):
    sent_messages = []
    for i in ds_tin_nhan:
        print(i)
        sent_messages.append(i)
    print(ds_tin_nhan)
    print(sent_messages)


ds_tin_nhan = ["Cau dang lam gi the?", "To dang thuc hanh python", "Kho khong cau oi?", "Huhu kho cau a :(("]
send_messages(ds_tin_nhan)
