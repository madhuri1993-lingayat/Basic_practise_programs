


val = [6,45,67,9,8,6,5,34,23,12,14,15,16,27]
print(val)
flag1 = False
flag2 = False

for item in val:
    print(item)
    if item%2==0:
        flag1=True
    else:
        flag2=True
    if flag1==flag2:
        break
if flag1 and flag2:
    print('None')
elif flag1:
        print('Even')
else:
        print('odd')

