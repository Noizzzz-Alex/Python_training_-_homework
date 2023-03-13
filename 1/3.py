number_1 = 2
number_2 = 2


def rec_sum(number_1, number_2, result=0):
    if number_1 == 0:
        if number_2 == 0:
            print(result)
            return
        else:
            result += 1
            rec_sum(number_1, number_2 - 1, result)
    else:
        result += 1
        rec_sum(number_1 - 1, number_2, result)


rec_sum(2, 2)
