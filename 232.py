def gcv(a, b):
    if b == 0:
        return a
    return gcv(b, a % b)

print(gcv(21, 42))