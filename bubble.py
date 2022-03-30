a = [14, 7, 53, 71, 9, 13, 5, 8, 10]


def bubble(a):
    for j in range(0, len(a) - 1):
        for i in range(0, len(a) - 1 - j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        print(a)


bubble(a)
