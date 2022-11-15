# Write your solution here

def formatted(Number_list:list):

    string_list = []
    
    for i in Number_list:

        z = round(i, 2)
        x = str(z)
        p = x.find(".")
        print(p)
        if len(x) < 4:
            x += "0"
    
        string_list.append(x)

    return string_list


if __name__ == "__main__":
    Numb_list = [0.99999]
    print(formatted(Numb_list))
