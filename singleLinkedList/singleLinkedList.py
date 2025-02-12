#Author: Maria Esteban
#Date: 01/29/2025
#Purpose: play around with linked lists adding and removing nodes, sorting and reversing the linked list... 

'''
Checks the user input. If is not an integer it gives an 
error message and lets the user try again. If user inputs a 'B', it 
goes back to Menu
'''
def inputCheck(prompt):
    while True:
        user_input=input(prompt)
        if user_input.upper() == 'B':
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer or 'B' to go back.")

class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        print("The new node has successfully been added")

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        print("The new node has successfully been added")

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node
        print("The new node has successfully been added")

    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node  
            if succeeding_node == None: # Remove last item
                self.tail = None
        elif current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None: # Remove tail
                self.tail = current_node
        print("Node has been successfully removed")

    ''' 
    Displays the contents of the linked list
        i.e   35--->95--->42
    '''
    def display(self):
        node=self.head
        if node == None:
            print("List is empty")
        while node != None:
            print(node.data, end=' ')
            if node.next != None:
                print("-->", end=' ')
            node=node.next
        print()

    ''' 
    Reverses a singly-linked list by reversing the pointers
    '''
    def reverse(self):
        prev = None
        curr = self.head

        while (curr != None):
            next = curr.next
            curr.next=prev
            prev=curr
            curr=next

        self.head = prev
        print("The list has been succesfully reversed")

    '''
    Counts the items in the singly linked list
    '''
    def count(self):
        count=0
        node = self.head
        while node != None:
            count+=1
            node=node.next
        print(f"The list has {count} elements")

    ''' 
    Searches a list for a value and rerturns the node where the first occurence of the value 
    happens or reruns None is the value wasn't found. Will be needed by Insert After and Remove After
    '''
    def ListSearch(self, value):
        node=self.head
        while node != None:
            if node.data == value:
                return node
            else:
                node=node.next
        return None

    '''
    Create a function to return a boolean value indicating whether
    the linked list is empty. This can replace if self.head == None in code.
    '''
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    '''
    Empties the linked list.
    '''
    def empty(self):
        self.head = None
        print("The list is now empty")

    '''
    Sorts the linked list using insertion sort
    '''
    def insertion_sort_singly_linked(self):
        before_current = self.head
        current_node = self.head.next
        while current_node != None:
            next_node = current_node.next
            position = self.find_insertion_position(current_node.data)
            if position == before_current:
                before_current = current_node
            else:
                self.remove_after(before_current)
                if position == None:
                    self.prepend(current_node)
                else:
                    self.insert_after(position, current_node)
            current_node = next_node
        print()
        print("Linked list is sorted")

    def find_insertion_position(self, data_value):
        position_a = None
        position_b = self.head
        while (position_b != None) and (data_value > position_b.data):
            position_a = position_b
            position_b = position_b.next
        return position_a
    

    '''
    Create a menu-driven program that allows the user to perform the following operations:
    Append, Prepend, Insert After, Remove After, Display, Reverse, Count, Exit
    '''
aList = LinkedList()  # Creates an empty linked list
done = False
while not done:
    print("\nMenu\n")
    print("A - Append")
    print("Z - Append multiple consecutive numbers")
    print("P - Prepend")
    print("I - Insert After")
    print("R - Remove After")
    print("E - Empty List")
    print("D - Display List")
    print("V - Reverse List")
    print("C - Count List Items")
    print("S - Sort List")
    print("Q - Quit Program")
    choice = input(":: ")
    choice = choice.upper() 

    if choice == 'A':
        nodeData = inputCheck("Enter a integer for node data (or 'B' to go back):")
        if nodeData != None:
            aList.append(Node(nodeData))
    
    elif choice == 'Z':
        i = inputCheck("From (type 'B' to go back):")
        if i == None:
            continue
        j = inputCheck("To (type 'B' to go back):")
        if j == None:
            continue
        for x in range (i,j+1):
            aList.append(Node(x))

    elif choice == 'P':
        nodeData = inputCheck("Enter a integer for node data (or 'B' to go back):")
        if nodeData != None:
            aList.prepend(Node(nodeData))

    elif choice == 'I':
        aList.display()
        nodeData = inputCheck("Enter a integer for node data (or 'B' to go back):")
        if nodeData == None:
            continue
        valueToSearch = inputCheck("Enter the value of the node after which the new node should be inserted (or 'B' to go back):")
        if valueToSearch == None:
            continue
        targetNode = aList.ListSearch(valueToSearch)
        if targetNode != None:
            aList.insert_after(targetNode, Node(nodeData))
        else:
            print(f"Node with value {valueToSearch} not found. Insertion failed.")

    elif choice == 'R':
        aList.display()
        valueToSearch= inputCheck("Enter the value of the node after which the next node should be removed (or 'B' to go back):")
        if valueToSearch == None:
            continue 
        targetNode = aList.ListSearch(valueToSearch)
        if targetNode != None:
            aList.remove_after(targetNode)
        else: 
            print(f"Node with value {valueToSearch} not found. Removal failed.")

    elif choice == 'E':
        aList.empty()

    elif choice == 'D':
        aList.display()

    elif choice == 'V':
        aList.reverse()

    elif choice == 'C':
        aList.count()

    elif choice == 'S':
        aList.insertion_sort_singly_linked()

    elif choice == 'Q':
        done = True