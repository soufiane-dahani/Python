ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list[1] = "World!"

ft_tuple = list(ft_tuple)
ft_tuple[1] = "France!"

ft_set = list(ft_set)
ft_set[0] = "Hello" # fix problem (set have no order)
ft_set[1] = "Paris!"

ft_dict = list(ft_dict)
ft_dict.append("42Paris!") # list does not take the value of key

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)



# Expected output:
# $>python Hello.py | cat -e
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$
# $>