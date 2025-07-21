import math

def remove_spaces(s):
    string_without_spaces = ""
    for a in s:
        if a == " ":
            pass
        else:
            string_without_spaces += a
    return string_without_spaces

def encryption(s):
    # Write your code here

    length = len(string_without_spaces)
    column = math.ceil(length ** (1/2))
    row = math.floor(length ** (1/2))
    if length > column * row:
        row += 1

    output = ""
    for b in range(1, column + 1):
        for c in range(1, row + 1):
            index = column*(c-1) + b
            if index > length:
                pass
            else:
                output += string_without_spaces[index - 1]
        output += " "

    return output

if __name__ == '__main__':
    s = 'have a nice days'

    string_without_spaces = remove_spaces(s)
    result = encryption(s)

    print(result)
