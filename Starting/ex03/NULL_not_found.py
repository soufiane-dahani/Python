def NULL_not_found(object: any) -> int:
    if type(object) == type(None):
        print("Nothing:", "None",type(object))
    elif str(object) == "nan":
        print("Cheese:", "nan",type(object))
    elif object == 0 and type(object) == int:
        print("Zero: 0", type(object))
    elif type(object) == str and object == "":
        print("Empty:", type(object))
    elif type(object) == bool:
        print(f"Fake: {object}", type(object))
    elif isinstance(object, str):
        print("Type not found")
    return 1

