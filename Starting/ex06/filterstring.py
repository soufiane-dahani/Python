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
            raise AssertionError("AssertionError: the arguments are bad 2")
        i += 1


def filterstring(string , number):
    string = string.split(" ")
    # list1: list = [item for item in string if len(item) >= int (number)]
    fn = lambda x: len(x)>= int(number)
    list1: list = [item for item in string if fn(item)]
    return list1



if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        else :
            ft_building(sys.argv[1])
            ft_building(sys.argv[2])
            if not isinstance(sys.argv[1], str):
                raise AssertionError("AssertionError: the arguments are bad")
            if not isinstance(sys.argv[2], int):
                raise AssertionError("AssertionError: the arguments are bad")
            print(filterstring(sys.argv[1], sys.argv[2]))
    except AssertionError as error:
        print(error)