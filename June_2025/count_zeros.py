def count_zeros(list_a, targ_ele):
    count_targ=0
    for item in list_a:
        if item==targ_ele:
            count_targ=count_targ+1
        #print("loop count ", count_zero)
    
    print("target element count is :", count_targ)


list_1=[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
targ_ele=0
#func call
count_zeros(list_1, targ_ele)

