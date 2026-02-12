import sys
print("__name__ is:", __name__)
if __name__ == "__main__":
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 2:
        try:
            number = int(sys.argv[1])
            print("My number is:", number)
            if number % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            print("AssertionError: argument is not an integer")
    else:
        print("AssertionError: more than one argument is provided")
