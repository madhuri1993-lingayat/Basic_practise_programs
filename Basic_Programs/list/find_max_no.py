import random
import sys




list = [random.randint(1,100) for i in range((30))]
print(list)
min = min(list) # using built in function max
print('min no in list is',min)

sys.exit()
list = [random.randint(1,100) for i in range((30))]
print(list)
max = max(list) # using built in function max
print('max no in list is',max)



sys.exit()
def min_from_list():
    list = [random.randint(1,100) for i in range((30))]
    print (list)

    min = list[0]
    for ele in list:
        if ele < min:
            min=ele
    print('minimum/samll no in list is',min)
    return min
m = min_from_list()


sys.exit()
def max_from_list():
    list = [random.randint(1,100) for i in range((30))]
    print (list)
    max =0
    for ele in list:
        if ele > max:
            max=ele
    print('maximum/largest no in list is',max)
    return max
m = max_from_list()

#print small no in list


