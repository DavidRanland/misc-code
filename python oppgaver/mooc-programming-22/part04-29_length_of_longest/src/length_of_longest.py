# Write your solution here


def length_of_longest(Llist):

    longest =[]

    for i in Llist:

        longest.append(len(i))
        
    x = max(longest)
    return x



if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)
    