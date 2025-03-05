def binary_search():
    print("Загадайте число от 0 до 1000.")
    print("Отвечайте на вопросы программы только 'да' или 'нет'.")

    min = 0
    max = 1000

    while min <= max:
        middle = (min + max) // 2

        answer = input(f"Твое число равно {mid}? (да/нет): ").strip().lower()
        if answer == 'да':
            print(f"Вы загадали число {mid}!")
            return
        elif answer != 'нет':
            print("Пожалуйста, введите 'да' или 'нет'.")
            continue

        answer = input(f"Твое число больше {mid}? (да/нет): ").strip().lower()
        if answer == 'да':
            min = middle + 1
        elif answer == 'нет':
            max = middle - 1
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")
            continue

    print("Что-то пошло не так. Попробуйте еще раз!")


if __name__ == "__main__":
    binary_search()