class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def enqueue(self,ele):
        new_node = Node(ele)
        if self.rear is None:
            self.front = self.rear = new_node
            self.size += 1
            return 
        self.rear.next = new_node
        self .rear = new_node
        self.size +=  1
    def dequeue(self):
        if self.isEmpty():
            return "THe Queue is EMpty"
        temp = self.front
        self.front = temp.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return temp.value
    def peek(self):
        if self.isEmpty():
            return "The Queue is Empty"
        return self.front.value
    def isEmpty(self):
        return self.size == 0
    def iterate(self):
        temp = self.front
        while temp:
            print(temp.value , end ="->")
            temp = temp.next


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.iterate()           # Output: 10->20->30->
print(q.dequeue())    # Output: 10
print(q.peek())       # Output: 20
q.iterate()