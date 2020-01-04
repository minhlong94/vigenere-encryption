"""A simple Vigenere encryption that uses ASCII to encrypt. As usual, Vigenere encrypts only alphabet characters
so it does not encrypt non-alphabet characters: every non-alphabet character returns itself."""


def encryption(text_char, key_char):
    rowplace = ord(text_char)
    if rowplace in range(97, 123):
        row = ord(text_char) - 97
        col = ord(key_char) - 65
        return chr((row + col) % 26 + 65)
    elif rowplace in range(65, 91):
        row = (ord(text_char) + 32) - 97
        col = ord(key_char) - 65
        return chr((row + col) % 26 + 65)
    else:
        return chr(rowplace)


def vigenere(text, key):
    key_letter = [c for c in key]
    text_letter = []
    output = []
    space = []
    for i in range(len(text)):
        if text[i] == " ":
            space.append(i)
        else:
            text_letter.append(text[i])

    if len(key) < len(text):
        for i in range(len(text) - len(key)):
            key_letter.append(key_letter[i])
    elif len(key) > len(text):
        for i in range(len(key) - len(text)):
            key_letter.pop(len(key_letter) - 1)

    for i in range(len(text_letter)):
        output.append(encryption(text_letter[i], key_letter[i]))
    for c in space:
        output.insert(c, " ")
    encrypted = ''.join(output)
    return encrypted


print("Welcome to Vigenere encryption.")
i = "1"
while i == "1":
    while True:
        try:
            key = input("Input your desired key: \nNote: it must not contains a blank.\n")
            for c in key:
                if c == " ":
                    raise Exception
        except Exception:
            print("Key contains blank character. Please input again.\n")
        else:
            break

    text = input("Input text you want to encrypt: \n")
    print("Your encrypted message is: {}\n".format(vigenere(text, key)))
    i = (input("Input ""1"" to continue, anything else to exit: \n"))
    if i != "1":
        exit()
