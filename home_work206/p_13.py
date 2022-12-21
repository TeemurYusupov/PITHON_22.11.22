def where(f, col):
    return [x for x in col if f(x)]        


data = '1 2 3 4 5 6 23 56 67'.split()

res = map(int, data)
res = where(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)