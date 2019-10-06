def guess(name1,name2):
	flames = {'f': 'friend', 'l': 'love','a': 'affection','m': 'marry','e': 'enemy','s': 'bro/sis'}
	list1 = []
	list2 = []
	similar = []
	
	#copying string into list
	for value in name1:
		list1.append(value)
	for value in name2:
		list2.append(value)
	print('List one is below')
	print(list1)
	print('\n')
	print('List two is below')
	print(list2)
	print('\n')
	
	#length of list1 and 2
	len1 = len(list1)
	len2 = len(list2)
	
	#cancellation step initializations
	list1_copy = list1[:]
	i = 0
	j = 0
	
	#cancellation loop
	while i < len1:
		j = 0
		while j < len2:
			value1 = list1[i]
			value2 = list2[j]
			if value1 == value2:
				list1.insert(i+1,'0')
				list1.remove(value1)
				list2.insert(i+1,'0')
				list2.remove(value2)
				i = i + 1
				j = j + 1
			else:
				j = j + 1 
		i = i + 1
	
	#removing 0 of lists
	while '0' in list1:
		list1.remove('0')

	while '0' in list2:
		list2.remove('0')
	
	#final list to flame
	final = list1 + list2
	final_string = ''
	
	#converting it back to a string
	for value in final:
		final_string = final_string + value
	print('Final string after cancellation')
	print(final_string)
	print('\n')

	#finding length of string
	length = len(final_string)
	
	i = 0
	while 1:
		for key,value in list(flames.items()):
			i = i + 1
			if (length) == i:
				del flames[key]
				i = 0
				if len(flames) == 1:
					return flames
					

inp1 = input('Enter the first name :')
inp2 = input('Enter the second name :')
ans = guess(inp1,inp2)
print(ans) 

