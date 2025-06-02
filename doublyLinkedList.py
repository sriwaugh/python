class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class Link:
    def __init__(self):
        self.head = None
    def append(self,ele):
        new = Node(ele)
        if self.head is None:
            self.head = new
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def prepend(self,ele):
        new = Node(ele)
        if self.head is None:
            self.head = new
            return
        new.next = self.head 
        self.head.prev = new
        self.head = new
    

    def delete(self,ele):
        curr = self.head
        while curr:
            if curr.data == ele:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return 
            curr = curr.next

    def display(self):
        temp = self.head
        while temp :
            print(temp.data,end="<->")
            temp = temp.next

    def displayback(self):
        curr = self.head
        if curr is None:
            return "Queue is empty"
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.data , end="<->" if curr.prev else '')
            curr = curr.prev