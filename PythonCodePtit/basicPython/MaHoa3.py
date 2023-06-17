# ch: character, step: int
def rotateCharacter(ch, step):
    return chr((ord(ch) - 65 + step) % 26 + 65)


# s: str
def rotate(s):
    step = sum(ord(i) - 65 for i in s)
    return ''.join(rotateCharacter(ch, step) for ch in s)


# s1, s2: str
# merge via s1
def merge(s1, s2):
    return ''.join(rotateCharacter(value, ord(s2[index]) - 65) for index, value in enumerate(s1))


# drive code
for _ in [0] * int(input()):
    s = input();
    n = len(s) // 2
    print(merge(rotate(s[:n]), rotate(s[n:])))