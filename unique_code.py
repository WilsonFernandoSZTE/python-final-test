def unique_code(text):
    code = ""
    for letter in text:
        code += str(ord(letter))
    return code