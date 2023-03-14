def get_input():
    text = input("What would you like me to convert? ")
    return text


def morse_code_converter(text):
    dict = {
        "A": "·− ",
        "B": "−··· ",
        "C": "−·−· ",
        "D": "−·· ",
        "E": "· ",
        "F": "··−· ",
        "G": "−−· ",
        "H": "···· ",
        "I": "·· ",
        "J": "·−−− ",
        "K": "−·− ",
        "L": "·−·· ",
        "M": "−− ",
        "N": "−· ",
        "O": "−−− ",
        "P": "·−−· ",
        "Q": "−−·− ",
        "R": "·−· ",
        "S": "··· ",
        "T": "− ",
        "U": "··− ",
        "V": "···− ",
        "W": "·−− ",
        "X": "−··− ",
        "Y": "−·−− ",
        "Z": "−−·· ",
        "0": "−−−− ",
        "1": "·−−−− ",
        "2": "··−−− ",
        "3": "···−− ",
        "4": "····− ",
        "5": "····· ",
        "6": "−···· ",
        "7": "−−··· ",
        "8": "−−−·· ",
        "9": "−−−−· ",
        " ": " / ",
    }

    if all(x.isalnum() or x.isspace() for x in text):

        text = text.upper()
        morse_code = ""

        for letter in text:
            morse_code = morse_code + dict[letter] + " "

        print(morse_code)

    else:
        print("Please only use letters and numbers")
        return (morse_code_converter(get_input()))


morse_code_converter(get_input())
