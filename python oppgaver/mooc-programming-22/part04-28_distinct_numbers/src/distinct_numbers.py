# Write your solution here



def distinct_numbers(number_list:list):
    
    Taken = []

    for i in number_list:

        if i not in Taken:
            Taken. append(i)
    Taken.sort()
    return Taken


if __name__ == "__main__":
    ogga = [2,1,1,1,1,1,3,3,2,2,4,4,5,5,6,6,]
    print(distinct_numbers(ogga))