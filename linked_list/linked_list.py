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
            print('current is none')
            return 'None'
        else:
            print('found current', current.data)
            output = ''
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
            