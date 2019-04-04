from linked_list import LinkedList

l = LinkedList()
print('start')

# # # Print initial state
# print('empty:')
# l.print()

# # # add()
# print('\n\n# add()')
# l.add('I\'m the HEAD, index 0')
# l.print()

# # delete()
ld1 = LinkedList()
print('\n\n# delete()')
ld1.add('I\'m the HEAD, index 0')
ld1.add('I\'m index 1')
ld1.add('I\'m index 2')
ld1.add('I\'m index 3')
ld1.add('I\'m index 4')
ld1.print()    
print('\n deleting at 1')
ld1.delete(1)
ld1.print()

# delete()
ld2 = LinkedList()
print('\n\n# delete()')
ld2.add('I\'m index 1')
ld2.add('I\'m index 2')
ld2.add('I\'m index 3')
ld2.add('I\'m index 4')
ld2.print()    
print('\n deleting at 0')
ld2.delete(0)
ld2.print()



# # insert()
# l2 = LinkedList()
# print('\n\n# insert()')
# l2.add('I\'m the HEAD, index 0')
# l2.add('I\'m index 1')
# l2.add('I\'m index 2')
# l2.add('I\'m index 3')
# l2.add('I\'m index 4')
# l2.print()
# l2.insert('INSERTED AT 3',3)
# l2.print()

# l3 = LinkedList()
# l3 = LinkedList()
# print('\n\n# insert()')
# l3.print()
# l3.insert('INSERTED AT 3 with empty list',3)
# l3.print()