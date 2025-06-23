l1=[1,5,3,4,5,6]
s1=set(l1)
print(s1)

seen=set()
first_repeating=None

for num in l1:
    if num in seen:
        first_repeating=num
        break

    seen.add(num)

if first_repeating is not None:
    print('First repeating is', first_repeating)

else:
    print("No repeating element")


    


