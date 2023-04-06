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


def calculate(data_list):
    d1 = list.__getitem__(data_list, 0)
    d2 = list.__getitem__(data_list, 1)
    h = list.__getitem__(data_list, 2)
    v_sand = list.__getitem__(data_list, 3)
    n = list.__getitem__(data_list, 4)
    theta1 = list.__getitem__(data_list, 5)
    x = math.tan(theta1 * nu.pi / 180) * d1
    l1 = math.sqrt(x ** 2 + d1 ** 2) * (3 / 5280)
    l2 = math.sqrt(((h - x) * (3 / 5280)) ** 2 + (d2 / 5280) ** 2)
    return [theta1, 1 / (v_sand / 3600) * (l1 + n * l2)]


list1 = interface_input()
list2 = calculate(list1)
print(f"Если спасатель начнёт движение под углом theta1, равным {round(list2.__getitem__(0))} "
      f"градусам, он достигнет утопащего через {round(list2.__getitem__(1), 1)} секунды")
