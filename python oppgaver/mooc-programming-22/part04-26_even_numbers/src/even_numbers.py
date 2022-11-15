# Write your solution here


def even_numbers(my_list:list):

    New_list = []

    for i in my_list:

        if i % 2 == 0:

            New_list.append(i)

    return New_list




if __name__ == "__main__":
    my_list = [1, 2,4,5,6,7,8]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)