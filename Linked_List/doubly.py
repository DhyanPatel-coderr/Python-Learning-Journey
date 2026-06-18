class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
head = None

def ask_data():
    data = int(input("Enter node value : "))
    return data

def ask_pos():
    pos = int(input("Enter position to insert/delete a value before/after the position : "))
    return pos

def insertAtbeginning():
    global head
    new_node = node(ask_data())

    if head is None:
        head = new_node
    else:
        new_node.next = head
        head.prev = new_node
        head = new_node
    print("Node inserted at front successfully")

def insertAtend():
    temp = head

    new_node = node(ask_data())

    if temp is None:
        insertAtbeginning()
    else:
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp 
        print("Node inserted at end successfully")

def insertBefpos(pos):
    temp = head

    if head is None:
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
            if temp is None:
                print("Position does not exist")
                return

            temp = temp.next
            count += 1
        if temp is None:
            print("Position does not exist")
            return
        
        new_node.next = temp.next
        temp.next.prev = new_node
        new_node.prev = temp
        temp.next = new_node

        print(f"Node inserted before position {pos} successfully")

def insertAftpos(pos):
    global head
    new_node = node(ask_data())
    temp = head

    if head is None:
        print("List is empty")
        return
    
    if pos <= 0:
        print("Enter valid position")
        return
    
    else:
        count = 1

        while count <= pos-1:
            if temp is None:
                print("Position does not exist")
                return
            temp = temp.next
            count += 1
        
        if temp is None:
            print("Position does not exist")
            return
        
        if temp.next is None:
            temp.next = new_node
            new_node.prev = temp
            print(f"Node inserted after position {pos} successfully")
            return
        
        temp.next.prev = new_node
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp

        print(f"Node inserted after position {pos} successfully")

def delFirstnode():
    global head

    if head is None:
        print("List is empty")
        return
    else:
        head = head.next 

        if head:
            head.prev = None
        print("First node deleted successfully")   

def delBefpos(pos):
    temp = head

    if head is None:
        print("List is empty")
        return
    
    if pos <= 0:
        print("Enter valid position")
        return
    
    elif pos == 1:
        print("There's no element to delete before position 1")
        return
    
    elif pos == 2:
        delFirstnode()
        return
    
    else:
        count = 1

        while count < pos-1:
            if temp is None:
                print("Position does not exist")
                return
            temp = temp.next 
            count += 1

        if temp is None:
            print("Position does not exist")
            return
        
        if temp.next is None:
            temp.prev.next = None
            print(f"Node deleted before position {pos} successfully")
            return
        
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
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
            if temp is None:
                print("Position does not exist")
                return
            temp = temp.next
            count += 1
        
        if temp is None:
            print("Position does not exist")
            return
        
        if temp.next is None:
            print("There's no element after this position to delete")
            return
        
        if temp.next.next is None:
            temp.next = None
            print(f"Node deleted after position {pos} successfully")
            return
        
        temp.next = temp.next.next
        temp.next.prev = temp
        print(f"Node deleted after position {pos} successfully")

def display():
    temp = head

    while temp:
        print(temp.data, end = " <-> ")
        temp = temp.next
    print("None")

def display_reverse():
    temp = head

    if temp is None:
        print("List is empty")
        return
    
    while temp.next:
        temp = temp.next
    
    while temp:
        print(temp.data, end = " <-> ")
        temp = temp.prev
    print("None")

while True:
    print("\n1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at before given node")
    print("4. Insert at after a given node")
    print("5. Delete first node")
    print("6. Delete node before a specified position")
    print("7. Delete a node after a specified position")
    print("8. Display")
    print("9. Reverse display")
    print("10. Exit")

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
        display_reverse()

    elif choice == 10:
        print("\nExiting Program...")
        exit()
        break