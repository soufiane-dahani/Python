import sys

def morse_code(str):
    NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
    }
    i = 0
    for i in range (len(str)):
        print(NESTED_MORSE[str[i].upper()], end="")
    print("")

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        else:
            i = 0
            for i in range (len(sys.argv[1])):
              if not sys.argv[1][i].isspace() and not sys.argv[1][i].isupper() and not sys.argv[1][i].islower() and not sys.argv[1][i].isdigit():
                  raise AssertionError("AssertionError: the arguments are bad")
              i += 1
            morse_code(sys.argv[1])
    except AssertionError as error:
        print(error)

