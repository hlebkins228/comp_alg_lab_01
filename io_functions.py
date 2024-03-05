from config import PointValues, accuracy


def read_data_from_file(filename: str) -> list[PointValues]:
    function_data = list()

    with open(filename, "r") as file:
        for line in file.readlines():
            line_values = list(map(float, line.split()))
            line_data = PointValues(x=line_values[0], derivatives=line_values[1:])

            function_data.append(line_data)
    
    return function_data


def input_value(prompt: str, value_type: type, greater_then_zero: bool):
    while True:
        try:
            n = value_type(input(prompt))
        except ValueError:
            print("\n>>> Некорректный ввод! <<<")
        else:
            if greater_then_zero and n < 0:
                print("\n>>> значение должно быть больше 0! <<<")
            else:
                return n


def input_data():
    n = input_value("\nвведите степень для полинома Ньютона: ", int, True)
    nodes_count = input_value("\nвведите кол-во узлов для полинома Эрмита: ", int, True)
    x = input_value("\nвведите x: ", float, False)

    return n, nodes_count, x


def print_ans(ans: float, type: int):
    print(f"\n{'Newton: ' if type == 1 else 'Hermit: '}\n--------\nf(x) = {round(ans, accuracy)}\n--------")


def __input_data_filename__() -> str:
    while True:
        filename = input("\ninput data file name: ")
        try:
            file = open(filename, "r")
        except (FileNotFoundError, FileExistsError) as exception:
            print(f"\n---- {exception} ----\n")
        else:
            return filename
