import tkinter


def add(*num):
    a = 0
    for n in num:
        a += n
    print(a)


add(5, 3, 2, 9)
