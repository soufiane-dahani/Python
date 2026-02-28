def count_in_list(lst : list, str) :
    total = 0
    for i in lst:
        if i == str:
            total +=1
    return total
