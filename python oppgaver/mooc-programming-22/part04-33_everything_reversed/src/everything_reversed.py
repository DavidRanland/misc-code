# Write your solution here



def everything_reversed(list: list):

    new_list = []

    for i in list[::-1]:

        x = i[::-1]
        new_list.append(x)
    return new_list


