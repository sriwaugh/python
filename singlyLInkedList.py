class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Link:
    def __init__(self):
        self.head = None
    def append(self, ele):
        new_node = Node(ele)
        if self.head is None:
            self.head = new_node
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def prepend(self,ele):
        new_node = Node(ele)
        new_node.next = self.head  
        self.head = new_node

    def delete(self,key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return 
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
    
l = Link()
l.append(10)
l.append(20)
l.prepend(5)
l.traverse()     # Output: 5->10->20->None
l.delete(10)
l.traverse() 