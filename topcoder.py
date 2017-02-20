import sys
import trie as Trie

T = Trie.Trie()

word = 'abcd'
T.insert(word)
T.insert('abpq')
T.insert('lmn')
T.insert('apqrs')
T.insert('abcdpqrs')
#a = T.prefix('ab')
a = T.count()
print(list(a))
for i in a:
	print(i)
#print(num)
print('')
#print('Word Count')

a = T.printword()
print(list(a))

print('')
s = 'ab'
print('Prefix',s)
T.prefix(s)
#print('prefix',s)
#print(a)
