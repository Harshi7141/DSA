class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None

    def insert_first_node(self,data):
        new_node=Node(data,self.start)
        self.start=new_node

    def insert_last_node(self,data):
        new_node=Node(data)
        if self.start is not None:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            if self.is_empty():
                self.start=new_node
            else:
                temp.next=new_node

    def search(self,data):
        if not self.is_empty():
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    return temp
                temp=temp.next

    def insert_after(self,temp,data):
        if temp is not None:
            new_node=Node(data,temp.next)
            temp.next=new_node

    def print_list(self):
        if not self.is_empty():
            temp=self.start
            while temp is not None:
                print(temp.item,end=' ')
                temp=temp.next

    def delete_first_node(self):
        if not self.is_empty():
            self.start=self.start.next

    def delete_last_node(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp.next=temp.next.next
                temp=temp.next

    def delete_Specific_node(self,data):
        if self.is_empty():
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            while temp.next is not None:
                if temp.next.item ==data:
                    temp.next=temp.next.next
                    break
                    temp=temp.next

mylist=SLL()
mylist.insert_first_node(10)
mylist.insert_after(mylist.search(10),20)
mylist.insert_last_node(30)
mylist.insert_last_node(40)
mylist.print_list()
print()
mylist.delete_Specific_node(20)
mylist.print_list()
print()