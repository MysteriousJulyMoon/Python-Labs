
def restore_string(s):
    result = ""
    text = ""

    for char in s:
        if char.isdigit():
            text += char
        else:
            if text:
                result += int(text) * char
                text = ""
            else:
                result += char

    return result


s = input()
restored_string = restore_string(s)
print(restored_string)