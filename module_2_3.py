my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = my_list[0]
index = 1
while index <= len(my_list):
    if number >= 0:
        if number != 0:
            print(number)
            number = my_list[index]
            index += 1
        else:
            number = my_list[index]
            index += 1
            continue
    else:
        break







