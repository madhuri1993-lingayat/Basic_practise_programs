import random
import sys

def multi_list(): #def fun
    list = [random.randint(1,10) for i in range(5)]
    print(list)
    total=1 #set counter initial zero
    for x in list: # for loop

        total *=x
    print(' multi of list ele are',total)
    return total
c =multi_list()


sys .exit()
#program sum of list ele using randon values
def sum_list(): #def fun
    list = [random.randint(1,20) for i in range(5)]
    print(list)
    total=0 #set counter initial zero
    for x in list: # for loop
        total +=x
    print('sum of list ele are',total)
    return total
c =sum_list()



