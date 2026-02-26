def ft_filter(function, iterable):
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))


# numbers = [1, 2, 3, None, 5, 6]


# def is_even(n):
#     return n % 2 == 0


# values = [0, 1, "", "hello", None, True, False]

# print(list(ft_filter(None, numbers)))


# for item in iterable:
#     yield item

# def count():
#     yield 1
#     yield 2
#     yield 3


# ( what_to_return  for loop_variable in iterable  if condition )
