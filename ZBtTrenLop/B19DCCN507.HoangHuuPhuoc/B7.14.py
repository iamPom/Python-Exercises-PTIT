# Bài 7.14 - B19DCCN507 Hoàng Hữu Phước
def make_car(*args, **kwargs):
    car_info = {}
    car_info["manufacturer"] = args[0]
    car_info["model"] = args[1]
    for key, val in kwargs.items():
        car_info[key] = val
    return car_info


print(make_car('subaru', 'outback', color='Red', tow_package=True))
