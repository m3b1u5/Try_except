# Exception handling

def calc():

    try:
        first_digit = float(input("Enter first digit: "))
        second_digit = float(input("Enter second digit: "))
        result = first_digit / second_digit

    except ValueError:
        print("Ошибка - введено некорректное число")
    except ZeroDivisionError:
        print("Ошибка деления на ноль")

    else:
        print(f"Результат: {result}")

    finally:
        print("Завершено\n")
        calc()

calc()