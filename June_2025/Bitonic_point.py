"""
Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the bitonic point, that is the maximum element in the array.
Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing.

Note: It is guaranteed that the array contains exactly one bitonic point.

Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 8
Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing [3].

"""

list_1=[1,2,4,5,6,8,3]

def bitonic_point(list_1):
    
    i=0
    res=0
    
    while (i<len(list_1)-1):
        
        print(i)

        print("ele 1",list_1[i])
        print("ele 2",list_1[i+1])
        diff=(list_1[i+1]-list_1[i])
        
        if (diff >0):
            i=i+1
            print("incremented i value is ", i)
        
        elif (diff <0):
            print("negative of res:")
            res=list_1[i+1]
            break

        print("this res value")
        res=list_1[i]

    return res

list_new=[10,20,30,50]
print(bitonic_point(list_new))



