# Write your solution here
# You can test your function by calling it within the following block

def first_word(word):

    i = word.find(" ")
    return word[:i]

def second_word(word):

    i = word.find(" ")
    pord = word[i+1:]
    i = pord.find(" ")
    if i == -1:
        return pord
    else:
        return pord[:i]
    
def last_word(word):
    i = ""
    o = -1
    new = ""
    while i != " ":
        
        i = word[o]
        o -= 1
        new += i
    x = ""
    for i in range(len(new)):
        
        x += new[(1+i)*(-1)]
    return (x[1:])


if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))