def rem(lst, value):
	try:
  		lst.remove(value)
  	except ValueError:
  		pass

'''
list1 = [1,2,3]
list1.remove(2)
print list1
rem(list1, 2)
print list1
'''

def enqItemFreq(D, item):
	#print D
	if not item in D:
		D[item] = 1
	else:
		before = D[item]
		D[item] += 1
	#print D
	#print "\n"
def deqItemFreq(D, item):
	#print D
	if not item in D:
		pass
	else :
		before = D[item]
		if before == 1:
			del D[item]
		else:
			D[item] -= 1
	#print D
	#print "\n"
def deleteItem(D, item):
	#print D
	if item in D:
		del D[item]
	#print D
	#print "\n"

#d = {}
#enqItemFreq(d, 'aaa')
#enqItemFreq(d, 'aaa')
#enqItemFreq(d, 'bbb')
#deleteItem(d, 'aaa')

