SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 1, 2, 3, 4


def check_lists(one, two):
    if one == two:
        return EQUAL

    len_1 = len(one)
    len_2 = len(two)

    if len_1 > len_2:
        for ii in range(len_1):
            if one[ii:len_2+ii] == two:
                return SUPERLIST

    for ii in range(len_2):
        if two[ii:len_1+ii] == one:
            return SUBLIST

    return UNEQUAL



