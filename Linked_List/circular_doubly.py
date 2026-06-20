class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
head = None

def ask_data():
    return int(input("Enter node value : "))

def get_last_node():
    temp = head

    while temp.next != head:
        temp = temp.next

    return temp

def ask_pos():
    return int(input("Enter position to insert/delete a node after/before position : "))

def get_length():
    temp = head
    length = 0

    while True:
        temp = temp.next
        length += 1

        if temp == head:
            break

    return length 

def insertAtbeginning():
    global head
    new_node = node(ask_data())

    if head is None:
        new_node.next = new_node
        new_node.prev = new_node
        head = new_node
        print("Node inserted at front successfully")
        return
    
    temp = get_last_node()

    new_node.next = head
    new_node.prev = temp
    temp.next = new_node
    head.prev = new_node
    head = new_node
    print("Node inserted at front successfully")

def insertAtend():
    global head

    if head is None:
        insertAtbeginning()
        return
    else:
        new_node = node(ask_data())
        temp = get_last_node()

        temp.next = new_node
        new_node.prev = temp
        new_node.next = head
        head.prev = new_node

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
        count = 1

        if pos > get_length() + 1:
            print("Position does not exist")
            return
        
        while count < pos-1:
            temp = temp.next
            count += 1
        
        if temp.next == head:
            insertAtend()
            return
        
        new_node = node(ask_data())
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

        print(f"Node inserted before position {pos} successfully")

def insertAftpos(pos):
    temp = head

    if temp is None:
        print("List is empty")
        return
    
    if pos <= 0:
        print("Enter valid position")
        return
    
    else:
        if pos > get_length():
            print("Position does not exist")
            return
        
        count = 1

        while count <= pos-1:
            temp = temp.next
            count += 1

        if temp.next == head:
            insertAtend()
            return
        
        new_node = node(ask_data())
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node

        print(f"Node inserted after position {pos} successfully")

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
        head.next.prev = head.prev
        head.prev.next = head.next
        head = head.next
    
        print("First node deleted successfully")

def delLastnode():
    global head
    temp = head

    if temp is None:
        print("List is empty")
        return
    
    elif temp.next == head:
        head = None
        print("Last node deleted successfully")
        return

    else:
        last = get_last_node()
        while temp.next != last:
            temp = temp.next
        
        temp.next = head
        head.prev = temp
        print("Last node deleted successfully")

def delBefpos(pos):
    temp = head

    if temp is None:
        print("List is empty")
        return
    
    if pos <= 0:
        print("Enter valid position")
        return
    
    elif pos == 1:
        delLastnode()
        return
    
    elif pos == 2:
        delFirstnode()
        return
    
    else:
        
        if pos > get_length():
            print("Position does not exist")
            return
        
        count = 1

        while count < pos-2:
            temp = temp.next
            count += 1
        
        temp.next = temp.next.next
        temp.next.prev = temp

        print(f"Node deleted before position {pos} successfully")

def delAftpos(pos):
    temp = head

    if temp is None:
        print("List is empty")
        return
    
    if pos <= 0:
        print("Enter valid position")
        return
    
    elif pos == get_length():
        delFirstnode()
        return
    
    elif pos > get_length():
        print("Position does not exist")
        return
    
    else:
        count = 1

        while count <= pos-1:
            temp = temp.next
            count += 1
        
        
        temp.next = temp.next.next
        temp.next.prev = temp

        print(f"Node deleted after position {pos} successfully")

def display():
    temp = head

    if temp is None:
        print("List is empty")
        return
    else:
        while True:
            print(temp.data, end = " <-> ")
            temp = temp.next

            if temp == head:
                break

def rev_display():

    if head is None:
        print("List is empty")
        return
    else:
        temp = get_last_node()
        while True:
            print(temp.data, end= " <-> ")

            if temp == head:
                break
            
            temp = temp.prev

while True:
    print("\n1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at before given node")
    print("4. Insert at after a given node")
    print("5. Delete first node")
    print("6. Delete last node")
    print("7. Delete node before a specified position")
    print("8. Delete a node after a specified position")
    print("9. Display")
    print("10. Reverse display")
    print("11. Exit")

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
        delLastnode()

    elif choice == 7:
        delBefpos(ask_pos())

    elif choice == 8:
        delAftpos(ask_pos())

    elif choice == 9:
        display()

    elif choice == 10:
        rev_display()

    elif choice == 11:
        print("\nExiting Program...")
        exit()
        break

    else:
        print("Enter valid choice")