import gauss, lagrange, newton


ys_gl = []

def solve(x, xs, ys):
    # Лагранж
    l = lagrange.lagrange(x, xs, ys, True)
    # Ньютон
    n = newton.newton_polynomial(x, xs, ys, True)
    # Гаусс
    g = gauss.gauss_interpolation(x, xs, ys, True)
    print("-" * 80)
    print("Результаты:")
    print(f"| Ньютона             | {n:10.6f}")
    print(f"| Лагранжа            | {l:10.6f}")
    print(f"| Гаусса              | {g:10.6f}")
    print("-" * 80)

    # Вывод графиков
    print("\nСтроим графики интерполяционных полиномов...")
    lagrange.plot_lagrange_polynomial(x, l, xs, ys)
    newton.plot_newton_polynomial(x, n, xs, ys)
    gauss.plot_gauss_polynomial(x, g, xs, ys)

    return [l, n, g]