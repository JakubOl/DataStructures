class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Allows to print yields each node
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creates node of value before/ after node
    def insertSLL(self, value, location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def searchSLL(self, value):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node:
                if node.value == value:
                    return print(node.value)
                node = node.next
            return print("Value not found")

    def deleteNode(self, idx):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            if idx == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = node.next
            elif idx == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < idx - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteSLL(self):
        self.head = None
        self.tail = None


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(0, 4)

# print([node.value for node in singlyLinkedList])
# singlyLinkedList.traverseSLL()
# singlyLinkedList.searchSLL(6)
print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteNode(0)
print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteSLL()
print([node.value for node in singlyLinkedList])
