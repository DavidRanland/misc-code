# Write your solution here


def shortest(Llist):

    longest =[]

    for i in Llist:

        longest.append(len(i))
        
    x = min(longest)
    
    for z in Llist:

        if  len(z) == x:
            return z



if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)
    