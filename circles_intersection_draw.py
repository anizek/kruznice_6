# circles_intersection_draw.py

import matplotlib.pyplot as plt


def draw_data(circle_1, circle_2):
    """
    Funkce vykreslí dvě kružnice do grafu.

    Parametry:
    - circle_1: slovník {"x": float, "y": float, "r": float}
    - circle_2: slovník {"x": float, "y": float, "r": float}
    """

    fig, ax = plt.subplots()

    # vytvoření a přidání kružnic
    k1 = plt.Circle((circle_1["x"], circle_1["y"]), circle_1["r"], fill=False, color="blue", label="Circle 1")
    k2 = plt.Circle((circle_2["x"], circle_2["y"]), circle_2["r"], fill=False, color="red", label="Circle 2")

    ax.add_patch(k1)
    ax.add_patch(k2)

    # stejné měřítko os, aby kružnice byly opravdu kruhy
    ax.set_aspect("equal")

    # automatické limity podle poloměrů a středů kružnic
    x_values = [circle_1["x"], circle_2["x"]]
    y_values = [circle_1["y"], circle_2["y"]]
    r_values = [circle_1["r"], circle_2["r"]]

    x_min = min(x - r for x, r in zip(x_values, r_values)) - 1
    x_max = max(x + r for x, r in zip(x_values, r_values)) + 1
    y_min = min(y - r for y, r in zip(y_values, r_values)) - 1
    y_max = max(y + r for y, r in zip(y_values, r_values)) + 1

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    # mřížka a legenda
    plt.grid(True)
    plt.legend()
    plt.show()