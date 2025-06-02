class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, element):
        new_node = Node(element)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    def pop(self):
        if self.isEmpty():
            return "THe Stack is Empty"
        poped = self.head
        self.head = self.head.next
        self.size -= 1
        return poped.value
    def peek(self):
        if self.isEmpty():
            return "The Stack is empty"
        return self.head.value
    def isEmpty(self):
        return self.size == 0
    def stacksize(self):
        return self.size
    def iterate(self):
        current = self.head
        while current:
            print(current.value, end = "->")
            current = current.next

    
mystack = stack()
mystack.push("1")
mystack.push("2")
mystack.push("3")
mystack.push("4")
mystack.iterate()
print(mystack.pop())
print(mystack.peek())

