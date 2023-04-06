import math
import numpy as nu


def interface_input():
    d1 = input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => ")
    d2 = input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => ")
    h = input("Введите боковое смещение между спасателем и утопающим, h (ярды) => ")
    v_sand = input("Введите скорость движения спасателя по песку, v_sand => ")
    n = input("Введите коэффициент замедления спасателя при движении в воде, n => ")
    theta1 = input("Введите направление движения спасателя по песку, theta1 (градусы) => ")
    return [float(d1), float(d2), float(h), float(v_sand), float(n), float(theta1)]


# Expression (formula) for time calculating: x^2 + (h-x)^2 is MIN!
def calculate(data_list, angle_list):
    d1 = list.__getitem__(data_list, 0)
    d2 = list.__getitem__(data_list, 1)
    h = list.__getitem__(data_list, 2)
    v_sand = list.__getitem__(data_list, 3)
    n = list.__getitem__(data_list, 4)
    theta1 = list.__getitem__(data_list, 5)
    x = math.tan(theta1 * nu.pi / 180) * d1
    l1 = math.sqrt(x ** 2 + d1 ** 2) * (3 / 5280)
    l2 = math.sqrt(((h - x) * (3 / 5280)) ** 2 + (d2 / 5280) ** 2)
    # Calculation with more efficient angle (auto)
    auto_x = list.__getitem__(angle_list, 1)
    auto_l1 = math.sqrt(auto_x ** 2 + d1 ** 2) * (3 / 5280)
    auto_l2 = math.sqrt(((h - auto_x) * (3 / 5280)) ** 2 + (d2 / 5280) ** 2)
    return [theta1, 1 / (v_sand / 3600) * (l1 + n * l2),
            1 / (v_sand / 3600) * (auto_l1 + n * auto_l2)]


def best_option(data_list):
    d1 = list.__getitem__(data_list, 0)
    h = list.__getitem__(data_list, 2)
    const_angle = 1
    x_const = math.tan(const_angle * nu.pi / 180) * d1
    expression = x_const ** 2 + (h - x_const) ** 2
    angle = 2
    const_x = 0
    while angle < 90:
        x = math.tan(angle * nu.pi / 180) * d1
        formula = x ** 2 + (h - x) ** 2
        if formula < expression:
            expression = formula
            const_angle = angle
            const_x = x
        angle += 1
    return [const_angle, const_x]


list1 = interface_input()
list2 = best_option(list1)
list3 = calculate(list1, list2)
print(f"Если спасатель начнёт движение под углом theta1, равным {round(list3.__getitem__(0))} "
      f"градусам, он достигнет утопащего через {round(list3.__getitem__(1), 1)} секунды")
print(f"Наиболее оптимальным уголом является угол, равный {list2.__getitem__(0)}, при котором спасатель "
      f"достигнет утопающего через {round(list3.__getitem__(2), 1)} секунды")
