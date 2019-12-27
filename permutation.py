from numpy.random import permutation

n = 8
N = 2**n

def eval_arx(f, x):
    for a, b in f:
        if a == 0: x = (x + b) % N
        if a == 1: x = ((x>>(n-b))|(x<<b)) % N
        if a == 2: x = x ^ b
    return x

def swap(a, b):
    if a == b: return []
    f = [(0, N-a)]
    a, b = 0, (b-a)%N
    while b & 1 == 0:
        f.append((1, n-1))
        b = b >> 1
    while b != 1:
        f.append((2, 1))
        b = b ^ 1
        f.append((0, N-1))
        b = (b + N-1) % N
    f.append((0, N-2))
    func = f + [(0,2), (1,n-1), (0,N-1), (1,1)]
    for a, b in reversed(f):
        if a == 0: func.append((0, N-b))
        if a == 1: func.append((1, n-b))
        if a == 2: func.append((2, b))
    return func

def gen_arx(p):
    dic = list(range(N))
    func = list()
    for i, x in enumerate(p):
        fs = swap(dic[i], x)
        func.extend(fs)
        j = dic.index(x)
        dic[i], dic[j] = dic[j], dic[i]
    return func


def main():
    p = permutation(N)
    f = gen_arx(p)
    for x, y in enumerate(p):
        yhat = eval_arx(f, x)
        assert y == yhat, "failed!"
    else:
        print("success!")

main()
