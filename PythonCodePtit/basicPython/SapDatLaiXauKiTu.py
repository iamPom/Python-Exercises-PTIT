t = int(input())
for i in range(1, t + 1):
    a = input()
    b = input()
    if sorted(a) == sorted(b):
        print("Test " + str(i) + ": YES")
    else:
        print("Test " + str(i) + ": NO")
