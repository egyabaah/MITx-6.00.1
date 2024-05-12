def printmove(start, dest):
    print("move from", start, "to", dest)


def Towers(n, start, dest, midd):
    if n == 1:
        printmove(start, dest)

    else:
        Towers(n - 1, start, midd, dest)
        Towers(1, start, dest, midd)
        Towers(n - 1, midd, dest, start)


Towers(20, "P1", "P2", "P3")
