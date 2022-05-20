import math
def f(N):
    numerator = N**N * math.exp(-N)
    denominator = ((N-1)/2)**((N-1)/2) * math.exp(-(N-1)/2) * ((N+1)/2)**((N+1)/2) * math.exp(-(N+1)/2)
    frac = numerator/denominator
    print(frac)
    f = 0.1
    return frac * (f**((N+1)/2)) * (1-f)**((N-1)/2)

for N in range(1, 100):
    error = f(N)
    if error < 10e-15:
        print(N)
        break

