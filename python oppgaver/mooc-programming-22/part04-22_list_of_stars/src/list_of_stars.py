# Write your solution here

def list_of_stars(numbers):

    for i in numbers:

        stars = ""
        
        for x in range(i):
            
            stars += "*"
        
        print(stars)


if __name__ == "__main__":

    number_list = [2,2]
    list_of_stars(number_list)
