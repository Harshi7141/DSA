class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None

    def insert_first_node(self,data):
        new_node=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=self.start
        self.start=new_node

    def insert_last_node(self,data):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            new_node=Node(temp,data,None)
            if temp==None:
                self.start=new_node
            else:
                temp.next=new_node

    def search(self,data):
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    return temp
                temp=temp.next
            return None

    def insert_after(self,temp,data):
        if temp is not None:
            new_node=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=new_node
            temp.next=new_node

    def print_list(self):
        if self.start is not None:
            temp=self.start
            while temp is not None:
                print(temp.item,end=' ')
                temp=temp.next

    def delete_first_node(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None

    def delete_last_node(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None

    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                        break
                temp=temp.next

mylist=DLL()
mylist.insert_first_node(10)
mylist.insert_after(mylist.search(10),20)
mylist.insert_last_node(30)
mylist.print_list()
print()
mylist.delete_item(20)
mylist.print_list()
