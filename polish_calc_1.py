input_string = input().strip()
string_arr = input_string.split()
stack = []
for char in string_arr:
    result = 0
    if char in "+-*":
        b = stack.pop()
        a = stack.pop()
        match char:
            case '+':
                result = a + b
            case '-':
                result = a - b
            case '*':
                result = a * b
        stack.append(result)
    else:
        stack.append(int(char))
print(stack[0])