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
    #removing end of element from the list
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head  
        while(temp.next):  #traversing the list and keeping track of prev for assigning tail before pop operation
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length -=1
        if self.length==0:  #this case is after poping single element the head and tail still referenced to the element
            self.head=None
            self.tail=None
        return temp.value  #returning poped value







#test cases
my_list=LinkedList(5)
my_list.append(4)
my_list.append(3)
my_list.print_list()
print('______')
print(my_list.pop())
print(my_list.pop())

