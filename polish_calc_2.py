input_string = input()
string_arr = input_string.split()
stack = []

for char in string_arr:
    result = 0
    if char in '+-*/':
        b = stack.pop()
        a = stack.pop()
        match char:
            case '+':
                result = a + b
            case '-':
                result = a - b
            case '*':
                result = a * b
            case '/':
                result = a // b
        stack.append(result)
    elif char in '~!#':
        a = stack.pop()
        match char:
            case '~':
                result = a * (-1)
            case '!':
                result = 1
                for i in range(1, a + 1):
                    result *= i
            case '#':
                stack.append(a)
                stack.append(a)
                continue
        stack.append(result)
    elif char == '@':
        c = stack.pop()
        b = stack.pop()
        a = stack.pop()
        stack.append(b)
        stack.append(c)
        stack.append(a)
    else:
        stack.append(int(char))
print(stack[0])