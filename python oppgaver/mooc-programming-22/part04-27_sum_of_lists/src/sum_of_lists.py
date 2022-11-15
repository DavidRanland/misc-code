# Write your solution here



def list_sum(list1:list, list2:list):

    new_list = []
    
    for i in range(len(list1)):

       x = list1[i] + list2[i]

       new_list.append(x)

    return new_list

if __name__=="__main__":

    list1 = [2,1,4]
    list2 = [3,9,1]

    print(list_sum(list1,list2))