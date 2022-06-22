# 1.- What is the difference between a list and a tuple?
# La diferencia entre una lista y una tupla, es que la lista se puede modificar
# despues de averce creado y la tupla no

# Lista 
my_list = [1,2,3]

# Diccionario
diccionario = {
	'key': 23,
  'admi': 'Cadena',
  '1': 1.2,
}

# Tupla 
my_tuple = (1, 2.4, 'a')

# Tupla dentro de otra tupla 
my_tuple = (1, 2.4, (1, 2,3))

my_list = [1,2,3,4]
my_tuple = ( 1, 2, 3, (3,4,5))

# 2.- Convet a list into a tuple
my_tuple = tuple(my_list)


# Resultado
print(my_tuple)
print(type(my_tuple))


# 3.- Print only values higher than 100
my_list = [100, 99, 101, 456, 83]
for item in my_list:
	if item > 100:
		print(item)


# 5.- Iterate my_list as a list comprehension 

"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

"""

#class Solution:
#    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
class Solution:
        def deleteDuplicates(self, my_list):
        	newList = []
	        for item in my_list:
        		if item not in newList:
        			newList.append(item)
        	return newList

head = [1,1,2]
s = Solution()
print(s.deleteDuplicates(head))
        
        
