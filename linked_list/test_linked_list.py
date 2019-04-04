from linked_list import LinkedList

l = LinkedList()
print('start')

# # Print initial state
print('empty:')
l.print()

# # add()
print('\n\n# add()')
l.add('I\'m the HEAD, index 0')
l.print()

# delete()
print('\n\n# delete()')
l.add('I\'m index 1')
l.add('I\'m index 2')
l.add('I\'m index 3')
l.add('I\'m index 4')
l.print()    
print('\n deleting at 1')
l.delete(1)
l.print()

# insert()
l2 = LinkedList()
print('\n\n# insert()')
l2.add('I\'m the HEAD, index 0')
l2.add('I\'m index 1')
l2.add('I\'m index 2')
l2.add('I\'m index 3')
l2.add('I\'m index 4')
l2.print()
l2.insert('INSERTED AT 3',3)
l2.print()

l3 = LinkedList()
l3 = LinkedList()
print('\n\n# insert()')
l3.print()
l3.insert('INSERTED AT 3 with empty list',3)
l3.print()