#tuples : ordered , immutable , allows duplication of element
#immutable --> cannot be changed after the creation of tuple
tuple1 = ("ruthra ", 18, "AI$DS", True, "RV")
print(tuple1)

single_tuple = ("ksrct")
print(type(single_tuple))
single_tuple1 = ("element",)  #--->if no comma it is considered as siring
print(type(single_tuple1))

#iteration in tuple
for i in tuple1:
    print(i)

if "ruthra" in tuple1:
    print("yes")
else:
    print("no")

#no of element in tuple
print(len(tuple1))

#count the element in tuple
rep_tuple = [1, 2, 3, 5, 4, 5, 6, 7, 9, 8, 2]
print("no of 5 is : ", rep_tuple.count(5))
print(rep_tuple.index(5)) #firstly avilable ndex position is mentioned

#convert the tuple into list
list_var = list(rep_tuple)
print(rep_tuple, type(rep_tuple))
#convert list to tuple
tuple_var = tuple(list_var)
print(tuple_var, type(tuple_var))
#slicing is as similar like in list the concept is similar in all the cases like string , list , tuple

#accessing the member element with specific name
my_tuple = ("Ruthravarshan", 18, "Avinashi")
name, age, city = my_tuple  #no of element specified should be equal to no.of elements in the tuple
print(name)
print(age)
print(city)

rep_tuple.sort()  #[1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
print(rep_tuple)

i1, *i2, i3, i4 = rep_tuple #tuple unpacking
print(i1)   #first element int he tuple
print(i3)   #last before element in the tuple
print(i2)   #between all element s inn the tuple till i3
print(i4)   #lastelement in tuple

# only two inbuild functions are there in tuples - count(),
