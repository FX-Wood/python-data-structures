import pytest
from linked_list import LinkedList

@pytest.fixture
def l_list():
    l = LinkedList()
    return l

@pytest.fixture
def list_4():
    l = LinkedList()
    l.add('I am the HEAD')
    l.add('I am index 1')
    l.add('I am index 2')
    l.add('I am index 3')
    return l

# Makes a list
def test_defined(l_list):
    assert l_list != None

# Test add()
def test_add_to_empty(l_list):
    l_list.add('I am the HEAD')
    assert l_list.head != None

def test_add_to_existing(l_list):
    l_list.add('I am the HEAD')
    l_list.add('I am index 1')
    assert l_list.head.pointer != None

# test get()
def test_get_from_empty(l_list):
    assert l_list.get(0) == []

def test_get_HEAD(list_4):
    assert list_4.get(0) == 'I am the HEAD'

def test_get_index_2(list_4):
    assert list_4.get(2) == 'I am index 2'

# test insert
def test_insert_at_0(l_list):
    l_list.insert('I am the HEAD', 0)
    assert l_list.head.data == 'I am the HEAD'

def test_insert_out_of_range_with_empty_list(l_list):
    l_list.insert('I am the HEAD', 10)
    assert l_list.head.data == 'I am the HEAD'

def test_insert_at_index(l_list):
    l_list.add('I am the HEAD')
    l_list.add('I am index 1')
    l_list.add('I am index 2')
    l_list.insert('I am insert @2', 2)
