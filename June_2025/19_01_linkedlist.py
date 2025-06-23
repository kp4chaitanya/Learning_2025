class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    
    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length=+1

#func call
my_linked_list=LinkedList(4)
#print(my_linked_list.head.value)
my_linked_list.print()

my_linked_list.append(5)
my_linked_list.print()
#print(my_linked_list.tail.value)
#print(my_linked_list.length.value)

