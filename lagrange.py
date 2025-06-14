import numpy as np
from matplotlib import pyplot as plt


def lagrange(x, xs, ys, show=False):
    if show: print("-----------------------------\n"
                   "Интерполяция Лагранжа")
    if len(xs) != len(ys):
        raise ValueError("Количество x и y значений должно совпадать!")


    result = 0.0
    n = len(xs)

    # Таблица конечных разностей
    delta = np.zeros((n, n))
    delta[:, 0] = ys
    for i in range(1, n):
        for j in range(n - i):
            delta[j, i] = delta[j + 1, i - 1] - delta[j, i - 1]

    if show:
        print("Таблица конечных разностей:")
        for row in delta:
            print(" ".join([f"{val:.3f}" for val in row]))

    for i in range(n):
        l = ys[i]  # Начинаем с y_i
        for j in range(n):
            if j != i:
                l*= (x - xs[j]) / (xs[i] - xs[j])  # Домножаем на (x - x_j)/(x_i - x_j)
        if show: print("L" + str(i) + ":", f"{float(l):.3f}")
        result += l
    if show: print("Результат:", f"{float(result):.3f}", "\n-----------------------------")

    return result


def plot_lagrange_polynomial(x, y, xs, ys, x_min=None, x_max=None, num_points=500):
    if x_min is None:
        x_min = min(xs) - min(xs) / 10
    if x_max is None:
        x_max = max(xs) + min(xs) / 10

    # Генерируем точки для построения графика
    x_vals = np.linspace(x_min, x_max, num_points)
    y_vals = [lagrange(x, xs, ys) for x in x_vals]

    # Настраиваем график
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="Интерполяционный полином Лагранжа", color="purple")
    plt.scatter(xs, ys, color="blue", label="Узлы интерполяции", zorder=5)
    plt.scatter([x], [y], color="red", zorder=5)
    plt.title("График интерполяции Лагранжа")
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()
    plt.show()