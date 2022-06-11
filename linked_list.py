class LinkedList:
    def __init__(self, item):
        self.head = item

    def toString(self):
        item = self.head
        items = []
        while item is not None:
            items.append(str(item.value))
            item = item.next
        items.append("None")
        return " -> ".join(items)

    # Insert function to add new element
    def insert(self, value):
        new_item = Item(value)
        item = self.head
        temp = None

        # Check if new element inserted at first position
        if value < item.value:
            new_item.next = item
            self.head = new_item    
            return

        temp = item
        item = self.head.next

        # Traverse through list until a bigger value is found
        while(item is not None):
            if item.value > value:
                # Use temp variable to switch pointers
                new_item.next = item
                temp.next = new_item
                return

            temp = item
            item = item.next

        # If no bigger value found, insert at the end
        temp.next = new_item
        
    # Search linked list to find element
    def search(self, value):
        item = self.head
        # Traverse through list until the value is found
        while(item is not None):
            if item.value == value:
                return

            item = item.next

    def delete_all(self):
        temp = None

        # Traverse through whole list
        while(self.head is not None):
            # Use temp variable to switch pointers
            temp = self.head.next
            del(self.head)
            self.head = temp

class Item:
    # Constructor definition
        def __init__(self, value):
            # Initialize pointers to next item with no target
            self.next = None
            # Set item value to value given as parameter
            self.value = value