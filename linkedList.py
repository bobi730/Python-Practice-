class Node:
    value=None
    next = None

    def __init__(self, value):
        self.value = value

class LinkedList:
    first=None
    last=None

    def add_last(self,item):
        node=Node(item)
        if self.first is None:
            self.first=node
            self.last=node
        else:
            self.last.next=node
            self.last=node

    def addFirst(self,item):
        node=Node(item)
        if self.first is None:
            self.first=node
            self.last=node
        else:
            node.next=self.first
            self.first=node

    def indexOf(self,item):
            i=0
            current=self.first
            while current is not None:
                if current.value==item:
                    return i
                i=i+1
                current=current.next
            return -1

    def contains(self,item):
        if self.indexOf(item)==-1:
            return False
        return True

    def delete_first(self):
        newFirst=self.first.next
        self.first.next=None
        self.first=newFirst

    def getPrev(self,node):
        current=self.first
        while current is not None:
            if current.next == node:
                return current
            current = current.next
        return None


    def deleteLast(self):
        newLast=self.getPrev(self.last)
        newLast.next=None
        self.last=newLast

    def lprint(self):
        current=self.first
        while current is not None:
            print(current.value)
            current=current.next

    def length(self):
        i = 0
        current = self.first
        while current is not None:
            i = i + 1
            current = current.next
        return i

    def addAfter(self,item,index):
        if index>=self.length() or index<0:
            print("Error, index out of bounds, no changes made.")
            return False
        current = self.first
        for i in range(0,index):
            current=current.next
        node=Node(item)
        forNext=current.next
        current.next=node
        node.next=forNext

    def deleteAt(self,index):
        if index>=self.length() or index<0:
            print("Error, index out of bounds, no changes made.")
            return
        current = self.first
        for i in range(0,index-1):
            current=current.next
        temp=current.next
        current.next=temp.next
        temp.next=None

    def getAt(self,index):
        try:
            current = self.first
            for i in range(0,index):
                current=current.next
        except:#erro name
            print()
        return current.value

    def setAt(self,num,index):
        if index >= self.length() or index < 0:
            print("Error, idex out of bounds, no changes made.")
            return False
        current = self.first
        for i in range(0, index):
            current = current.next
        current.value=num


l=LinkedList()
l.addLast(5)
l.addLast(4)
l.addFirst(2)
l.addFirst(23)
l.addFirst(3)

l.lprint()