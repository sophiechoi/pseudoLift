class Pair:
	left = None
	right = None
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __repr__(self):
		return "("+str(self.left)+", "+str(self.right)+")"

class Triple:
	fst= None
	snd= None
	trd= None
	def __init__(self, fst, snd, trd):
		self.fst = fst
		self.snd = snd
		self.trd = trd
	def __repr__(self):
		return "("+str(self.fst)+", "+str(self.snd)+", "+str(self.trd)+")"

'''
print Pair(1, 3)
print Triple(1,3,4)
p1 = Pair(1,3)
p2 = Pair(2,3)
ps = [p1, p2]

print ps
psss = [x for x in ps if x.left == 1]
print psss
#ps.remove(Pair(1,3))
#ps.remove(p1)
for i in range(len(psss)):
	ps.remove(psss[i])

print ps
'''