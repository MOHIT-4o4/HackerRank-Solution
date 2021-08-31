'''Creating a Node'''


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


'''Creating Linked list that contains node'''


class linkedList:
    def __init__(self):
        self.head = None
    def printlist(self, head):
        temp = head
        while (temp):
            print(temp.data, "->")
            temp = temp.next

    def newNodeAtEnd(self, head, data):
        if head == None:
            head = node(data)
        else:
            temp = head
            while(temp.next):
                temp = temp.next
            temp.next = node(data)
        print("Node Inserted at End")

    def reverse(self, head):
        curr = head
        if curr == None:
            return
        elif(curr.data % 2 == 0 and curr.next.data % 2 == 0):
            curr, curr.next = curr.next, curr
            print("changed")
        else:
            curr = +1
        print("run")


'''Execute the code'''

llt = linkedList()
   
T = int(input())
for i in range(T):
        data = int(input())
        head=llt.newNodeAtEnd(head, data)
        # llt.printlist(head)
llt.printlist(head)
llt.reverse(head)
llt.printlist(head)
