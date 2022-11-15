# Write your solution here


def anagrams(word,word1):

    sort_word = sorted(word)
    sort_word1 = sorted(word1)

    if sort_word == sort_word1:
        return True
    else:
        return False




if __name__ == "__main__":
    somthing = "house"
    somthing1 = "esuoh"
    print(anagrams(somthing,somthing1))
    