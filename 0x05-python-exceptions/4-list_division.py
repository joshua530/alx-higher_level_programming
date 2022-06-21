#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            tmp = float(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            tmp = 0
        except TypeError:
            print("wrong type")
            tmp = 0
        except IndexError:
            print("out of range")
            tmp = 0
        finally:
            res.append(tmp)
    return res
