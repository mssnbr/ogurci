def is_valid_expression(expression):
    stack = []
    for a in expression:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
def decode_commands(expression):
    while '(' in expression:
        start = expression.rfind('(')
        end = expression.find(')', start)
        inner = expression[start + 1:end]
        decoded = ''
        i = 0
        while i < len(inner):
            if inner[i].isdigit():
                num = int(inner[i])
                i += 1
                command = inner[i]
                decoded += command * num
            else:
                decoded += inner[i]
            i += 1
        expression = expression[:start] + decoded + expression[end + 1:]
    return expression
def main():
    while True:
        user_input = input("Введите закодированные команды: ")

        if is_valid_expression(user_input):
            result = decode_commands(user_input)
            print("Результат:", result)
            break
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")
#никакие библиотеки не использовались