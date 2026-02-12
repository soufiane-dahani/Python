def all_thing_is_obj(object: any) -> int:   
    if type(object) == list:
        print("List :", type(object))
    elif type(object) == tuple:
        print("Tuple :", type(object))
    elif type(object) == set:
        print("Set :", type(object))
    elif type(object) == dict:
        print("Dict :", type(object))
    elif isinstance(object, str):
        print(f"{object} is in the kitchen :", type(object))
    elif isinstance(object, int):
        print("Type not found")
    return 42

    

# list2 = ["Hello", "tata!"]

# ft_tuple = ("Hello", "toto!")

# if type(ft_tuple) == tuple:
#     print("tuple" , end=" ")
#     print(type(ft_tuple))
