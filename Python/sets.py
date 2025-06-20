# sets : unordered , mutable , collection datatype , no duplicates

set1 = {1, 2, 3, 4, 5}  # basic method t define a set
print(set1)
set2 = set("Hello")  # the sets in default ordered , and remove duplicate
print(set2)
set3 = set()  # only by this way empty set can be given
# using {} to define empty set will not define as set it will define as dictionary
# .`. set is mutable elements can be added in it -easily
set3.add(1)
set3.add("hi")
print(set3)
set1.remove(1)
print(set1)
set1.discard(1)  #do same as remove but if the element is not found nothing is cared...no error is passed
print(set1)

set2.clear() #to clear the entire set and return empty set
print(set2)

print(set1.pop()) #here in case of list it removes first element

for i in set1:   #basic iteration of elements
    print(i)

#chk the presence of item
if 2 in set1:
    print("yes")
else:
    print("no")  #hence no item found there
#```````````````````OPERATIONS IN SET``````````````````
odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

oANDe = odd.union(even)  #combines all the set items
print(oANDe)

i = odd.intersection(prime)
print(i)               #common elements in both the set are included

diff = odd.difference(prime)
print(diff)    #element in A but not in B

sym_diff = odd.symmetric_difference(prime)
print(sym_diff)  #print all except common elements

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
setB = {1, 2, 3, 10, 11, 12}
setD = {1, 2, 3, 10, 11, 12}
setC = {20, 30, 40, 50}
setA.update(setB)  #update setA with extra elements in set B
print(setA)
setA.difference_update(setB)  #update setA with only difference element
print(setA)
setA.symmetric_difference_update(setB)
print(setA)
print(setA.issubset(setB))  #if all elements in A is in B
print(setB.issubset(setA))  #if all elements in B is in
print(setB.issuperset(setD))  #exctly the same elements in both set
print(setB.isdisjoint(setC))  #not even single item in single in both set

settA = {1, 2, 3, 4, 5, 6}  
settB = settA  #assigning value of the one set to another simple will change the original set also
settB.add(7)
print(settB)
print(settA)

settC = settA.copy()  #copy function do not change the original set
#settC = set(settA) #using set function also won't change the original set
settC.add(8)
print(settC)
print(settA)

frozensettt = frozenset([1, 2, 3, 4])
frozensettt.add(5) #cannot change the frozen set
frozensettt.remove(1) #cannot change the frozen set

