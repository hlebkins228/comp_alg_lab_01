from prettytable import PrettyTable

from comp_functions import *
from io_functions import *


def action_input() -> int:
    while True:
        try:
            action = int(input("Введите действие: "))
        except ValueError:
            print("\n>>> Некорректный ввод! <<<\n")
        else:
            if action < 0 or action > 4:
                print("\n>>> Такого действия нет! <<<\n")
            else:
                return action


def print_menu():
    print("\n0) интерполяция Ньютона и Эрмита\n1) сравнение полиномов\n"
          "2) найти корень функции\n3) решить систему уравнений\n4) выход\n")


def task_0(data: list[PointValues]):
    n, nodes_count, x = input_data()

    if nodes_count > len(data):
        print("\n>>> Недостаточно данных для построения полинома с заданным кол-ом узлов! <<<\n")
    elif n + 1 > len(data):
        print("\n>>> Недостаточно данных для построения полинома заданной степени! <<<\n")
    elif x < data[0]['x'] or x > data[-1]['x']:
        print("\n>>> Введенный аргумент находится вне диапозона! <<<\n")
    else:
        ans_hermit = calculate_ans_hermit(data, x, nodes_count)
        ans_newton = calculate_ans_newton(data, x, n)

        print_ans(ans_hermit, 2)
        print_ans(ans_newton, 1)


def task_1(data: list[PointValues]):
    user_x = input_value("\nвведите x: ", float, False)

    table = PrettyTable()
    empty_column = '-----'
    table.field_names = ['nodes_count', 'hermit', empty_column, 'n', 'newton']

    for n in range(1, 6):
        table.add_row([n, round(calculate_ans_hermit(data, user_x, n), accuracy), empty_column
                          , n, round(calculate_ans_newton(data, user_x, n), accuracy)])

    print(table)


def task_2(data: list[PointValues]):
    print(f"\nкорень полинома Ньютона = {newton_reverse_interpolation(data)}")
    print(f"\nкорень полинома Эрмита = {hermit_reverse_interpolation(data)}\n")


def task_3(data_1: list[PointValues], data_2: list[PointValues]):
    new_data_table = list()
    for current_point in data_1:
        current_x = current_point['x']
        y_1 = current_point['derivatives'][0]
        y_2 = calculate_ans_newton(data_2, current_x, 4)

        new_data_table.append(PointValues(x=current_x, derivatives=[y_2 - y_1]))

    ans_x = newton_reverse_interpolation(new_data_table)
    ans_y = calculate_ans_newton(data_1, ans_x, 4)

    print(f"\nрешение системы уравнений = ({ans_x}, {ans_y})\n")


def main_menu():
    function_data_from_file = read_data_from_file('data/data_1.txt')
    task_3_data_1 = read_data_from_file('data/data_2.txt')
    task_3_data_2 = read_data_from_file('data/data_3.txt')

    while True:
        print_menu()
        action = action_input()
        if action == 0:
            task_0(function_data_from_file)
        elif action == 1:
            task_1(function_data_from_file)
        elif action == 2:
            task_2(function_data_from_file)
        elif action == 3:
            task_3(task_3_data_1, task_3_data_2)
        elif action == 4:
            print("\n--- exit ---")
            break


if __name__ == "__main__":
    main_menu()
