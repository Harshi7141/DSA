class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CSLL:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last==None

    def insert_first_node(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node
            self.last=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node

    def insert_last_node(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node
            self.last=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node
            self.last=new_node

    def search(self,data):
        if self.is_empty():
            return None

        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None

    def insert_after(self,temp,data):
        if temp is not None:
            new_node=Node(data,temp.next)
            temp.next=new_node
            if temp==self.last:
                self.last=new_node

    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp!= self.last:
                print(temp.item, end=" ")
                temp=temp.next
            print(temp.item)

    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
            while temp!=self.last:
                temp=temp.next
            temp.next=self.last.next
            self.last=temp

    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                if self.last.next.item==data:
                    self.delete_first()
                else:
                    temp = self.last.next
                    while temp!=self.last:
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.delete_last()
                                break
                        if temp.item==data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next

mylist = CSLL()
mylist.insert_first_node(10)
mylist.insert_after(mylist.search(10),20)
mylist.insert_last_node(30)
mylist.print_list()
#print()
#mylist.delete_item(20)
#mylist.print_list()
