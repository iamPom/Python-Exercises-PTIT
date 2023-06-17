def check(num, base):
    res = ""
    while num > 0:
        res += str(num % base)
        num //= base
    return res == res[::-1]


def check_bin(num):
    b = bin(num)[2:]
    return b == b[::-1]


# drive code
a, b, m = map(int, input().split())
nums = [x for x in range(a, b + 1) if check_bin(x)]
for base in range(3, m + 1):
    nums = [num for num in nums if check(num, base)]
    if len(nums) == 0: break
print(len(nums))
