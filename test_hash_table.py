import hashlib
from hash_table import HashTable

def hash_example(string):
    hash_key = hashlib.md5( string.encode() )
    hash_hex = hash_key.hexdigest()
    hash_int = int(hash_hex, 16)
    return {'hash_key': hash_key, 'hash_hex': hash_hex, 'hash_int': hash_int }

for item in hash_example('Hello World'):
    print(item)

t = HashTable(16)
t.insert('Carlo', 'This is Carlo\'s string')
t.insert('Complex Gavin', 'This is Gavin\'s string')
t.insert('Mickey', 'This is Mickey\'s string')
t.insert('FX', "this is FX's string")
t.insert('Mike', "This is Mike's string")
t.insert('Garrett Moore', "This is Garrett's string")
t.insert('Charles Yun', "This is Charles's string")
t.print_table()
foo = t.search('Charles Yun')
print(foo)