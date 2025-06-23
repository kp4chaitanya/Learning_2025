def second_largest_ele(my_list):
  my_list.sort()
  second_largest=my_list[-2]
  return second_largest


list_1=[1,2,3,4,5]
print(second_largest_ele(list_1))