def pow(A, B):
    if B == 0:
        return 1
    if B < 0:
        return 1 / pow(A, -B)
    if B % 2 == 0:
        return pow(A, B // 2) * pow(A, B // 2)
    else:
        return pow(A, B - 1) * A

A = int(input())
B = int(input())
print(pow(A, B))