def fact(n):
    if not n:
        return 1
    return n * fact(n - 1)

def roots(a, b, c):
    D = b ** 2 - 4 * a *c
    if D < 0:
        print('Нет корней.')
    elif D == 0:
        print(-b / 2 * a)
    else:
        print((-b + D ** 0.5) / 2 * a, (-b - D ** 0.5) / 2 * a)