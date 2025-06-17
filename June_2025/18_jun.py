print("Hello")

#List code

my_list=[]
for i in range(20):
    my_list.append(i)

print("Created List is: ", my_list)

filtered_list=[]

for item in my_list:
    if item >=6:
        filtered_list.append(item)

print("Filtered list elements are: ", filtered_list)
print("Number of elements in filtered list is ", len(filtered_list))


print("List new way of printing elements")
for index, value in enumerate(my_list):
    print(index, value)

print("Building a dictionary from list: ")
res=list(enumerate(my_list))
dict1=dict(res)
print(dict1)


#Dictionary

print("enumerate of my_list")
print(dict(enumerate(my_list)))


list_1=[0,5,10,15,20]
list_filter=[item for item in list_1 if item<10]
print("List comprehension resulted: ", list_filter)
dict_2=dict(enumerate(list_1))
print("dict_2 elements are: ")
print(dict_2)

"""
my_dict=my_list

print("Dictionary elements")
for item in my_dict:
    print(item)
"""


result=[]
for item, value in dict_2.items():
    if value>5:
        result.append(value)

print("Result: ", result)

#print("ITEMS",dict_2.items())
#print("VALUES",dict_2.values())

print("Dictionary comprehension")

res_dict= { value  for item,value in dict_2.items() if value>10 }
print("Dictionary comprehension results: ", res_dict)
print(type(res_dict))