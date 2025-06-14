from math import factorial
import numpy as np
import matplotlib.pyplot as plt



def gauss_interpolation(x, xs, ys, show=False):
    if show: print("-----------------------------\nИнтерполяция Гаусса")
    if len(xs) != len(ys):
        raise ValueError("Количество x и y значений должно совпадать!")

    n = len(xs)
    h = xs[1] - xs[0]

    for i in range(1, n - 1):
        if abs((xs[i + 1] - xs[i]) - h) > 1e-10:
            raise ValueError("Узлы должны быть равноотстоящими")

    # Центральный индекс
    m = n // 2
    t = (x - xs[m]) / h

    # Таблица конечных разностей
    delta = np.zeros((n, n))
    delta[:, 0] = ys
    for i in range(1, n):
        for j in range(n - i):
            delta[j, i] = delta[j + 1, i - 1] - delta[j, i - 1]

    if show:
        print("Таблица конечных разностей:")
        for row in delta:
            print(" ".join([f"{val:.5f}" for val in row]))

    result = delta[m, 0]

    if x < xs[m]:
        t = (x - xs[m]) / h
        product = 1
        for k in range(1, n):
            if k % 2 == 1:
                idx = m - (k + 1) // 2
            else:
                idx = m - k // 2
            if idx < 0 or idx + k >= n or idx >= n:
                break
            product *= (t + (-1) ** (k % 2) * (k // 2))
            term = product * delta[idx][k] / factorial(k)
            result += term
    else:
        t = (x - xs[m]) / h
        product = 1
        for k in range(1, n):
            idx = m - k // 2
            if idx < 0 or idx + k >= n or idx >= n:
                break
            product *= (t - (-1) ** (k % 2) * (k // 2))
            term = product * delta[idx][k] / factorial(k)
            result += term

    if show:
        print("Результат:", f"{float(result):.6f}", "\n-----------------------------")
    return result



def plot_gauss_polynomial(x, y, xs, ys, x_min=None, x_max=None, num_points=500):
    if x_min is None:
        x_min = min(xs) - min(xs) / 10
    if x_max is None:
        x_max = max(xs) + min(xs) / 10


    # Генерируем точки для построения графика
    x_vals = np.linspace(x_min, x_max, num_points)
    y_vals = [gauss_interpolation(x, xs, ys) for x in x_vals]

    # Настраиваем график
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="Интерполяционный полином Гаусса", color="black")
    plt.scatter(xs, ys, color="blue", label="Узлы интерполяции", zorder=5)
    plt.scatter([x], [y], color="red", zorder=5)
    plt.title("График интерполяции Гаусса")
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()
    plt.show()