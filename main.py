# Exception handling

# Создайте программу, которая:
# Запрашивает у пользователя ввод двух чисел.
# Пытается разделить первое число на второе.
# Обрабатывает следующие исключения:
# ValueError, если пользователь ввел нечисловое значение.
# ZeroDivisionError, если второе число равно нулю.
# В случае успешного выполнения операции выводит результат.
# Использует блок finally, чтобы вывести сообщение о завершении работы программы.

def calc():
    first_digit = float(input("Enter first digit: "))
    second_digit = float(input("Enter second digit: "))

    try:
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