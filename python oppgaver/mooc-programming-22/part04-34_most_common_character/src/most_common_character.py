# Write your solution here




def most_common_character(string):

    letter_list = []
    for i in string:

        counter = 0
        fstring = string
        x = i

        while x != -1:

            counter +=1
            x = fstring.find(i)
            fstring = fstring[x+1:]

        if str(letter_list).find(i) == -1:

            result = i+ str(counter-1)

            letter_list.append(result)

    number_list = []

    for x in letter_list:

        number_list.append(x[1])
    
    MAX = max(number_list)
    full_string = ""
    for x in letter_list:

        full_string += x

    index = full_string.find(str(MAX))
    
    return full_string[index-1]
