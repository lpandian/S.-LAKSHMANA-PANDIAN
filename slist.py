class Node:
    def __init__(self, Newdata=None):
        self.data = Newdata
        self.next = None
class SlinkedList:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def Atbeg(self, Newdata):
        NewNode = Node(Newdata)
        NewNode.next= self.head
        self.head =NewNode
    def Atend(self, Newdata):
        NewNode = Node(Newdata)
        x = self.head
        if(x == None):
            self.head =NewNode
            return
        while(x.next):
            x=x.next
        x.next =NewNode
    def Afterval(self, val, Newdata):
        NewNode = Node(Newdata)
        temp= self.head
        if(temp==None):
            print('empty list not found')
            return
        while(temp):
            if(temp.data == val):
                break
            temp=temp.next
        if(temp == None):
            print('val not found')
            return
        NewNode.next =temp.next
        temp.next =NewNode
            
list1 = SlinkedList()
e1 =Node(10)
list1.head =e1
e2 = Node(15)
e1.next=e2
e3 =Node(20)
e2.next=e3
list1.printlist()
list1.Atbeg(25)
print('After add 25 at begining')
list1.printlist()      
list1.Atend(50)
print('After add 50 at begining')
list1.printlist()
list1.Afterval(15,75)              
print('After add 75 after 15')
list1.printlist()

        
            








    
