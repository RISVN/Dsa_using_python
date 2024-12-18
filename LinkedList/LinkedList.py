class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList():
    #constructer
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    #method for printing the linkedlist
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    #method for appending the list
    def append(self,value):
        new_node=Node(value)
        if self.head is None:   #what if new_node.head?
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

my_list=LinkedList(5)
my_list.append(4)
my_list.print_list()