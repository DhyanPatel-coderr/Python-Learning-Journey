class node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = None

def ask_data():
    data = int(input("Enter node value : "))
    return data

def ask_pos():
    pos = int(input("Enter position to insert/delete a node after/before the position : "))
    return pos

def insertAtbeginning():
    global head
    new_node = node(ask_data())
    
    if head is None:
        new_node.next = new_node
        head = new_node 
        print("Node inserted at front successfully")
        return
    
    else:
        temp = head

        while temp.next != head:
            temp = temp.next

        temp.next = new_node    
        new_node.next = head
        head = new_node
    print("Node inserted at front successfully")

def insertAtend():
    temp = head

    if temp is None:
        insertAtbeginning()
        return
    
    else:
        new_node = node(ask_data())

        while temp.next != head:
            temp = temp.next

        new_node.next = head
        temp.next = new_node
        print("Node inserted at end successfully")

def insertBefpos(pos):
    temp = head

    if temp is None:
        print("List is empty")
        return
    
    if pos <= 0:
        print("Enter valid position")
        return 
    
    elif pos == 1:
        insertAtbeginning()
        return
    
    else:
        new_node = node(ask_data())
        count = 1

        while count < pos-1:
            temp = temp.next

            if temp == head:
                print("Position does not exist")
                return
            
            count += 1

        if temp.next == head:
            print("Position does not exist")
            return
        
        new_node.next = temp.next
        temp.next = new_node
        print(f"Node inserted at before position {pos} successfully")

def insertAftpos(pos):
    temp = head

    if temp is None:
        print("List is empty")
        return
    
    if pos <= 0:
        print("Enter valid position")
        return 
    
    else:
        count = 1

        while count <= pos-1:
            temp = temp.next

            if temp == head:
                print("Position does not exist")
                return
            
            count += 1
        
        if temp.next == head:
            insertAtend()
            return
        
        else:
            new_node = node(ask_data())

            new_node.next = temp.next
            temp.next = new_node

            print(f"Node inserted after the position {pos} successfully")   

def delFirstnode():
    global head
    temp = head

    if temp is None:
        print("List is empty")
        return
    
    elif temp.next == head:
        head = None
        print("First node deleted successfully")
        return
    
    else:
        while temp.next != head:
            temp = temp.next

        temp.next = head.next
        head = head.next
        print("First node deleted successfully")

def delBefpos(pos):
    global head
    temp = head

    if temp is None:
        print("List is empty")
        return

    if pos <= 0:
        print("Enter valid position")
        return 
    
    elif pos == 1:
    
        if head.next == head:
            head = None
            print("Node deleted before position 1 successfully")
            return
        
        while temp.next.next != head:
            temp = temp.next

        temp.next = head
        print("Node deleted before position 1 successfully")
        return 
    
    elif pos == 2:
        delFirstnode()
        return

    else:
        count = 1

        while count < pos-2:
            temp = temp.next

            if temp == head:
                print("Position does not exist")
                return

            count += 1
        if temp.next.next == head:
            print("Position does not exist")
            return
        
        temp.next = temp.next.next   
        print(f"Node deleted before position {pos} successfully") 

def delAftpos(pos):
    temp = head

    if temp is None:
        print("List is empty")
        return
    
    if pos <= 0:
        print("Enter valid position")
        return 
    
    else:
        count = 1
        while count <= pos-1:
            temp = temp.next

            if temp == head:
                print("Position does not exist")
                return
            
            count += 1
        if temp.next == head:
            delFirstnode()
            return
        temp.next = temp.next.next

def display():
    temp = head

    if temp is None:
        print("List is empty")
        return
    
    else:
        while True:
            print(temp.data, end = " -> ")
            temp = temp.next

            if temp == head:
                break
        print("head")

while True:
    print("\n1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at before given node")
    print("4. Insert at after a given node")
    print("5. Delete first node")
    print("6. Delete node before a specified position")
    print("7. Delete a node after a specified position")
    print("8. Display")
    print("9. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        insertAtbeginning()

    elif choice == 2:
        insertAtend()

    elif choice == 3:
        insertBefpos(ask_pos())

    elif choice == 4:
        insertAftpos(ask_pos())

    elif choice == 5:
        delFirstnode()

    elif choice == 6:
        delBefpos(ask_pos())

    elif choice == 7:
        delAftpos(ask_pos())

    elif choice == 8:
        display()

    elif choice == 9:
        print("\nExiting Program...")
        exit()
        break