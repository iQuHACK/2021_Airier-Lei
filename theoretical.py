

def res(n, size, trials):
    s = 0
    t = 0
    for i in range(trials):
        s += n % size
        t += 1
        if s >= size:
            return t
        n /= size
    return trials + 1

def theoretical(bits, trials):
    s = 0
    for i in range(2**(bits * trials)):
        s += res(i, 2**bits, trials)
    return s / 2 ** (bits * trials)

print(theoretical(4, 3))
