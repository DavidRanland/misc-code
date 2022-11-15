# Write your solution here



def all_the_longest(Llist:list):

    longest = []
    new_list = []

    for i in Llist:

        longest.append(len(i))
        
    x = max(longest)

    for z in Llist:

        if len(z) == x:

            new_list.append(z)

    return new_list

if __name__ == "__main__":
    LONG_list = ["pingu", "hama", "hamod", "tit"]
    print(all_the_longest(LONG_list))