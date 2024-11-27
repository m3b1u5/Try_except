# Exception handling

def get_num(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Ошибка - введено некорректное число")


def calc():
    try:
        first_num = get_num("Введите первое число: ")
        second_num = get_num("Введите второе число: ")
        result = first_num / second_num
    except ValueError:
        print("Ошибка - введено некорректное число\n")
    except ZeroDivisionError:
        print("Ошибка деления на ноль\n")
        calc()
    else:
        print(f"Результат: {result}")


def main():
    try:
        calc()
    finally:
        print("Завершено\n")


main()
