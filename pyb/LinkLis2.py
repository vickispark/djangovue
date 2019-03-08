class Node:
    def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

    def getData(self):
       return self.data

    def setData(self,val):
       self.data = val

    def getNextNode(self):
       return self.nextNode

    def setNextNode(self,val):
       self.nextNode = val

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def get_size(self):
        return self.__size

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data,self.__head)
        self.__head = new_node
        self.__size += 1
        return True

        # Remove pass and write the logic to add an element

    def display(self):
        curr = self.__head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()
        # Remove pass and write the logic to display the elements
    # You can use the below __str__() to print the elements of the DS object while debugging

    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.getData()))
            temp = temp.getNextNode()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


list1 = LinkedList()
list1.add("Sugar")
list1.add("Sugar2")
print("Element added successfully")

list1.display()
print(list1.__str__())

# Similarly add all the specified element(s)