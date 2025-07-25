class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next


#function calls
linked_list=LinkedList(4)

print("head",linked_list.head.value)
print("tail",linked_list.tail.value)
print("length",linked_list.length)
linked_list.print_list()