
# set s collection of unorder pport, ele, indexing not supported, seq not maintain,
# hash method used, immutable,single  none type alloweded
# unindexed
#duplicate not allowdeed

# set methods

s = {10,30,34,450,56,23,56,78,90,56,34}
print(len(s))
s1 = {23,46,56,4,3,5,6,7,8,9,1,2,3,4,5}
print(len(s1))
print(s)
print(s1)
pop = s.pop()
print(pop)
updte = s.update(s1)#s is  set 1 and s2 is set 2 , s is update by s1 values
print(updte)
print(s)
print(len(s))

s2 = {10,20,30,40,56,76}
s3 = {30,40,50,60,10,33,45,67,88,20}
print(s2,s3)
diff = s2.difference(s3) # difference means uncommon ele which only in s2 , [20,76,56]
print(diff)
dis = s2.discard(10)
print(dis,s2)
remove = s2.remove(20)
print(remove,s2)
intersection = s2.intersection(s3) # print common ele in both set
print(intersection)
inter_upd = s2.intersection_update(s3)
print(inter_upd)
isdijoin = s3.isdisjoint(s2) #common
print(isdijoin)
print(len(s3))
#update-- combine both-- keep unique one only
#difference --  A-B -- only those elements from A are not in B
#intersection -- A&B -- common -- shud present in both
#symetricdiffrn - A^B -- uncommon of both
union = s3.union(s2)
print(union)
sym_diff = s3.symmetric_difference(s2)
print(sym_diff)