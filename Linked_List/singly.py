class node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = None

def data_insert():
    data = int(input("Enter a node value to insert : "))
    return data

def ask_pos():
    pos = int(input("Enter position to insert/delete a value before/after the position : "))
    return pos

def insertAtbeginning():
    global head
    new_node = node(data_insert())

    new_node.next = head
    head = new_node

    print("Node inserted at front successfully")

def insertAtend():
    temp = head

    if temp is None:
        insertAtbeginning()
    else:
        new_node = node(data_insert())

        while temp.next is not None:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node 

        print("Node inserted at end successfully")

def insertBefpos(pos):
    new_node = node(data_insert())
    temp = head

    if pos <= 0:
        print("Enter valid position")
        return

    if temp is None:
        print("List is empty")
        return
    
    elif pos == 1:
        insertAtbeginning()
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
        
        new_node.next  = temp.next
        temp.next = new_node

        print(f"Node inserted before position {pos} successfully")

def insertAftpos(pos):
    temp = head
    new_node = node(data_insert())
    
    if pos <= 0:
        print("Enter valid position")
        return
    
    if temp is None:
        print("List is empty")
        return

    else:
        count = 0

        while count < pos -1 :
            if temp is None:
                print("Position does not exist")
                return
            temp = temp.next
            count += 1

        if temp is None:
            print("Position does not exist")
            return
        
        new_node.next = temp.next
        temp.next = new_node

def delFirstnode():
    global head
    temp = head

    if temp is None:
        print("List is empty..First insert something to delete")
        return
    else:
        head = head.next
        print("First node deleted successfully")

def delBefpos(pos):
    global head
    temp = head

    if temp is None:
        print("List is empty..First insert something to delete")
        return
    
    if pos <= 0:
        print("Enter valid position")
        return
    
    elif pos == 1:
        print("There's no element before position 1")
        return
    
    elif pos == 2:
        delFirstnode()
        print("Node before position 2 deleted successfully")
        return
    
    else:
        count = 1
        prev = temp
        while count < pos-1:
            if temp.next is None:
                print("Position does not exist") 
                return
            
            prev = temp
            temp = temp.next
            count += 1

        if temp.next is None:
                print("Position does not exist") 
                return
        
        prev.next = temp.next
        temp = temp.next

        print(f"Node before position {pos} deleted successfully")        

def delAftpos(pos):
    global head
    temp = head

    if temp is None:
        print("List is empty")
        return

    if pos <= 0:
        print("Enter valid position")
        return
    
    else:
        count = 0

        while count < pos-1:
            if temp.next is None:
                print("There's no element to delete after the last position") 
                return
            temp = temp.next
            count += 1
        
        if temp.next is None:
            print("There's no element after this position")
            return
        
        temp.next = temp.next.next
        print(f"Node after position {pos} deleted successfully")

def Display():
    temp = head

    if temp is None:
        print("List is empty")
    else:
        while temp is not None:
            print(temp.data, end = "->")
            temp = temp.next
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
        Display()

    elif choice == 9:
        print("\nExiting Program...")
        exit()
        break