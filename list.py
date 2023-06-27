"""
Node Class:
Every item in the linked list will be encapsulated in this class.
value:  the item encapsulated by the node.
next : a pointer to the next node in line. This will be None if it is the last item in the list.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Linked List Class:
The class that will be used to store items.
"""


class LinkedList:
    def __init__(self):
        self.root = None
        self.len = 0

    """
    add function: Adds an item to the linked list. 
    """

    def add(self, value):

        # encapsulates the value into a Node
        newNode = Node(value)

        # sets newNode to root if list is empty
        if self.len == 0:
            self.root = newNode
            self.len += 1

        # sets newNode to root's next Node if there is only a root node
        elif self.len == 1:
            self.root.next = newNode
            self.len += 1

        # if there are more than 1 Node, a loop places the newNode at the end of the list
        else:
            tempNode = self.root
            for i in range(0, self.len):
                if tempNode.next == None:
                    tempNode.next = newNode
                    self.len += 1
                    return self
                tempNode = tempNode.next
        # returns itself as a linked list
        return self

    """
    remove function: Removes an item from the list that has the same value as the provided value.
    This code excludes the possibility for duplicate items, so if match is found it is removed and loop is broken
    If there is not a node with the given value, the function does nothing.
    """

    def remove(self, value):

        # checks if the list is empty
        if self.len == 0:
            return self

        # if not empty, a tempNode is set to the root Node
        tempNode1 = self.root
        # checks if the root Node has the intended value for deletion
        if tempNode1.value == value:
            self.root = tempNode1.next
            self.len -= 1
            return self

        # Otherwise, loops through list until a match is found or end of list is reached with no match
        for i in range(0, self.len - 1):
            if tempNode1.next.value == value:
                tempNode1.next = tempNode1.next.next
                self.len -= 1
                break
            tempNode1 = tempNode1.next

        # returns itself as a linked list
        return self

    """
    size function: Returns the number of nodes in the list. Return 0 if the list is empty.
    """

    def size(self):
        return self.len

    """
    contains function: Returns True if the list has a node with the same value as the provided 
    value. Return False otherwise.
    """

    def contains(self, value):

        # checks if user entered no input and list is empty
        if self.len == 0 and value is None:
            return True

        # checks if the root is the intended Node
        if self.len != 0 and self.root.value == value:
            return True

        # Otherwise loops through entire list until match is found or end of list is reached without match
        tempNode = self.root
        for i in range(0, self.len - 1):
            if tempNode.next.value == value:
                return True
            tempNode = tempNode.next

        # returns false if no match was found
        return False

    """
    asList function: Returns the linked list as a python list.
    """

    def asList(self):
        # array used to store the values of the Nodes in a array format
        list = []

        # returns empty list if array is empty
        if self.len == 0:
            return list

        # returns list with only root value if the size of the list is 1
        elif self.len == 1:
            list.append(self.root.value)
            return list

        # If size of list is greater than one, loops through list appending values to list array
        else:
            list.append(self.root.value)
            tempNode2 = self.root.next
            for i in range(0, self.len - 1):
                if tempNode2.next == None:
                    list.append(tempNode2.value)
                    break
                else:
                    list.append(tempNode2.value)
                tempNode2 = tempNode2.next

        # returns the list after being populated by loop
        return list
