
#list:ordered , mutable , allow duplicate element

mylist = ["apple", "banana", "cheery", "apple"]  # allows duplication
print(mylist)
mylist2 = list()  # keyword list to define the empty list
print(type(mylist2))

print("")
mylist3 = [5, "ruthra", 100, True]  # contains multiple data types

#~~~~~~~~iterating the list element~~~~~~~~
for i in mylist3:
    print("list element", i, "---->", type(i))

#~~~~~~~~~~~~~~~~~~~ACCESSING THE LIST ELEMENTS~~~~~~~~~~~~~~~~~~~~~~~~~
item = mylist[0]
print(item)
print(item[-1])  # -ve indexing

#_________check the presence of the item in the list_________
if "banana" in mylist:
    print("yes")
else:
    print("no")

#----------find the no of elements in the list---------
print(len(mylist))

#+++++++++ managing list element ++++++++++++
mylist3.append("varshan")  # append at the end of the list
mylist3.insert(1, "AI&DS")  # inserting the element where we needed
print(mylist3)
mylist3.pop()  # last element is removed
print(mylist3)
mylist3.remove("ruthra")  # removing specific element in a list
print(mylist3)
mylist3.clear()
print(mylist3)  # clear the entire list
#//////////////////////////////////////////////////////////
mylist.reverse()  # reversing the list
print(mylist)
num = [1, 2, 10, -6, -4, 23, 5]
print(num)
num.sort()  # can sort data with same data type
print(num)

new_num = sorted(num)  # sort the list and save it in the new variable/list hence sorted returns a value
print(new_num)

#===================INTER MEDIATE METHODS IN LIST======================
l1 = [0] * 5
print(l1) #we get [0, 0, 0, 0, 0] //ASSIGN MULTIPLE SAME VALUES
l2 = [1, 2, 3, 4, 5, 6, 7, 8]
l3 = l1+l2 #[0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
print(l3)

#======slicing operator========[start index : stop index : step index]

print(l3[1]) #specific index element alone
print(l3[-1]) #sepecific element according to the negative indexing (starts from -1 in the last/end of the list)
print(l3[1:]) #from start till the end of the list members
print(l3[:10]) #from starting till the indexing 13
print(l3[1:5]) #element indexing from 1 to 5
print(l3[1:13:2]) #element from indexing 1 to 13 with 2 intervals
print(l3[::-1]) # best idea to reverse the string

list_original = ["ram", "sam", "vam", "cam"]
list_copy = list_original
print(list_copy)

list_copy.append("tom") # changes made to the copy of the list also changes the original string      !!!!!!(shares same memory)
print(list_copy)
print(list_original)  #checking...

original = ["bike", "car", "scoot", "bus"]
copy = list(original.copy())    #use list keyword to copy as list // tuples can be stored as list
#copy = original[:] copies the specified index element to the copy list
original.append("cycle")

print(original)
print(copy)

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i*i for i in a]    #[expression   for (variable) in (list_name)]

print(a)
print(b)  #print the square of the list in the

