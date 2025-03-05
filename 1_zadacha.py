def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    start = int(input())
    end = int(input())

    if start > end:
        print("Начало диапазона должно быть меньше или равно концу диапазона. Попробуйте снова.")
    elif start != int(start) and end != int(end):
        print("Некорректный ввод. Пожалуйста, введите целые числа.")

    break

primes = [num for num in range(start, end + 1) if is_prime(num)]

print(primes)
#никакие библиотеки не использовались