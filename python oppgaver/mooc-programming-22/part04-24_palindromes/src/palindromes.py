


def palindromes(word: str):
    return word == word[::-1]

def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            return True
        else:
            print("that wasn't a palindrome")

main()

if __name__ == "__main__":
    palindromes("word")
