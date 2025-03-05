def binary_search():
    print("Загадайте число от 0 до 1000.")
    print("Отвечайте на вопросы программы только 'да' или 'нет'.")

    low = 0
    high = 1000

    while low <= high:
        mid = (low + high) // 2

        answer = input(f"Твое число равно {mid}? (да/нет): ").strip().lower()
        if answer == 'да':
            print(f"Вы загадали число {mid}!")
            return
        elif answer != 'нет':
            print("Пожалуйста, введите 'да' или 'нет'.")
            continue

        answer = input(f"Твое число больше {mid}? (да/нет): ").strip().lower()
        if answer == 'да':
            low = mid + 1
        elif answer == 'нет':
            high = mid - 1
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")
            continue

    print("Что-то пошло не так. Попробуйте еще раз!")


if __name__ == "__main__":
    binary_search()
#никакие библиотеки не использовались