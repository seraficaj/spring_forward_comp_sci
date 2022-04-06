class Node:
	# constructor
	def __init__(self,data,next):
		self.data = data
		self.next = next

	def __str__(self): #tells python how to print this node
		return str(self.data)


class LinkedList:
	#constructor
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __str__(self):
		if self.size == 0:
			return '[]'

		current = self.head
		result = str(current) #result is the string version of current
		while current.next: # while there exists a next nod
			result += f', {str(current.next)}'
			current = current.next
		return f'[{result}]'
		
		
	# returns length of list
	def __len__(self):
		return self.size

	# same as append
	def insert_end(self, data):
		if self.size == 0:
			new_node = Node(data, None)
			self.head = new_node
			self.tail = new_node
			# self.head = Node(data, None)
			# self.tail = self.head
		else:
			temp = self.tail # stores old tail in temp
			self.tail = Node(data, None) #Creates new node and assigns it to tail
			temp.next = self.tail #set the OLD tail to point to new tail
		self.size += 1

	def remove(self, data):
		if self.size == 0: # case 1, empty list
			return 'Lis is already empty.'
		elif self.size == 1: # case 2, single-node-list
			if self.head.data == data:
				self.head = None
				self.tail = None
				self.size = 0
			else:
				return 'Item not found.'
		else: # case 3, 2+ nodes in the list
			if self.head.data == data: # delete the head
				old_head = self.head
				self.head = old_head.next
				old_head.next = None
				self.size -= 1
			else: # delete anything other than the head
				current = self.head
				while current.next:
					if current.next.data == data: # we've found the node to be deleted
						node_to_delete = current.next
						current.next = node_to_delete.next
						node_to_delete.next = None
						if current.next is None:
							self.tail = current
						self.size -=1
						return # mission accomplised!
					else: # continue the loop because we didn't find it yet
						current = current.next
				return 'Item not found.' # finished loop, didn't find it
						

my_list = LinkedList()
my_list.insert_end('Taylor')
my_list.insert_end('Jason')
my_list.insert_end('April')
my_list.insert_end('Weston')
print(my_list)

my_duplicates = [1,1,1,3,4,5,6,7,7,7]
print(set(my_duplicates))
