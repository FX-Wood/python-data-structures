from list_node import ListNode

class LinkedList():
    def __init__(self):
        self.head = None
    
    def add(self, data):
        if self.head == None:
            self.head = ListNode(data)
        else:
            current = self.head
            while current.pointer != None:
                current = current.pointer
            current.pointer = ListNode(data)
    
    def print(self, delimiter='-->'):
        current = self.head
        if current == None:
            return 'None'
        else:
            output = '\033[91mHEAD\033[00m: '
            while current != None:
                output += current.data + delimiter
                current = current.pointer
            output += f" \033[96mNone\033[00m"
            print(output)
    
    def delete(self, index):
        current = self.head
        if current == None:
            return Exception('Cannot delete from empty list')
        else:
            i = 0
            while i < index:
                if current.pointer == None:
                    return Exception('index out of range')
                current = current.pointer
                i += 1
            current.pointer = current.pointer.pointer
    
    def insert(self, data, index):
        current = self.head
        insert_index = 0
        if current == None:
            self.head = ListNode(data)
        else:
            while insert_index < index and current.pointer != None:
                current = current.pointer
                insert_index += 1
            new_node = ListNode(data)
            new_node.pointer = current.pointer
            current.pointer = new_node
        return insert_index