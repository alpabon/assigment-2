# Create a Node class to represent each customer in the waitlist
class Node:

    def __init__(self,value):
        self.name= value
        self.next= None
    

    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self,name):
        new_node=Node(name)
        new_node.next=self.head
        self.head=new_node

    def add_end(self,name):
        new_node=Node(name)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current= current.next
            current.next =new_node
        print(f"{new_node.name} added to the end of the waitlist")
   


    def print_list(self):
        if not self.head:
            print(f"The waitlist is empty")
            return
        else:
            current= self.head 
            print(f"Current waitlist ")
            while current:
                print(f"{current.name}")
                current=current.next
    
    def remove(self,name):
        current = self.head
        prev = None 

        if not current:
            return f"{name} not found"
        
        if current.name== name:
            self.head = current.next
            return f"{name} was removed"
        
        while current:
            if current.name == name:
                prev.next=current.next 
                return f"{name} was removed"
            prev = current
            current = current.next

        return f"{name} not found" 
        



    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
            print(f"{name} added to the front of the waitlist")
        
            # Call the add_front method
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
            # Call the add_end method
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            result = waitlist.remove(name)
            print(result)
            # Call the remove method
            
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()
            # Print out the entire linked list using the print_list method.
            
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program

waitlist_generator()
'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?

Design Memo:

The watilist is linked to a list, which each element that in this case is a Node contains data and a pointer to the next element in the list, in this case each node represents a costumer on the waitlist. my first class the linkedlist manages all the list by keeping in reference the first element that is called the head, new customers that can be added in the fron or the end of the list depends on the position of the header. When a customer is removed, it searchs in the list until the node with the matching name is found, and the previous node’s pointer is updated to skip over it, removing that customer from the waitlist.

The head plays a crucial role in this code because it always is keeping in reference the first element of the list, so without th ehead we wouldnt know which is the front or the end of the list.

An engineer might need a custom link list like this in situations where more data is need it to insert or is more dynamic to keep updating a simgle list, what I looked is that in an example of this is to manage processes in an operating system, or creating more efficient data buffers for network packets
'''
