import sys


def ft_building(object: any) -> int:
    i = 0
    number_up = 0
    number_low = 0
    number_spaces = 0
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
            raise AssertionError("AssertionError: the arguments are bad 2")
        i += 1


def filterstring(string, number):
    string = string.split(" ")
    try:
        number = int(number)
    except ValueError:
        raise AssertionError("AssertionError: the arguments are bad")
    list1 = [item for item in string if (lambda x: len(x) > number)(item)]
    return list1


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        else:
            ft_building(sys.argv[1])
            ft_building(sys.argv[2])
            if not isinstance(sys.argv[1], str):
                raise AssertionError("AssertionError: the arguments are bad 3")
            if not isinstance(sys.argv[2], str):
                raise AssertionError("AssertionError: the arguments are bad 4")
            print(filterstring(sys.argv[1], sys.argv[2]))
    except AssertionError as error:
        print(error)
