def Floor_ele_finder(list2, x):
    Less_than_or_eql_floor=[]
    for item in list2:
        print("1st loop ", item)
        if item <=x:
            Less_than_or_eql_floor.append(item)
            print("Less than eql floor list ", Less_than_or_eql_floor)

    Less_than_or_eql_floor.sort()
    floor_element=Less_than_or_eql_floor[-1]
    print("floor ele assigned as ", floor_element)

    floor_element_index=0
    for item in list2:
        print('second loop item', item)
        if item==floor_element:
            #print("index is ",list2.index(item))
            floor_element_index=list2.index(item)
        
    if floor_element_index is not None:
    
        print("Floor element index is ", floor_element_index)
    
    else:
        print("-1")

    
my_list=[1, 2, 8, 10, 10, 12, 19]
x=5
#Floor_ele_finder(my_list, x)

list_new= [1, 2, 8, 10, 10, 12, 19]
x1=11
Floor_ele_finder(list_new, x1)
Floor_ele_finder(list_new, x=0)
