import sys


def ft_building(object: any) -> int:
    i = 0
    number_up = 0
    number_low = 0
    number_spaces = 0
    number_other = 0
    total = 0
    number_digits = 0

    object = str(object)

    while object.__len__() > i:
        if object[i].isspace():
            number_spaces += 1
            total += 1
        elif object[i].isupper():
            total += 1
            number_up += 1
        elif object[i].islower():
            total += 1
            number_low += 1
        elif object[i].isdigit():
            total += 1
            number_digits += 1
        else:
            total += 1
            number_other += 1
        i += 1
    print(f"The text contains {total} characters:")
    print(f"{number_up} upper letters")
    print(f"{number_low} lower letters")
    print(f"{number_other} punctuation marks")
    print(f"{number_spaces} spaces")
    print(f"{number_digits} digits")


if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            raise AssertionError("Too many arguments")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        elif len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.read()
        ft_building(text)
    except AssertionError as error:
        print(error)
