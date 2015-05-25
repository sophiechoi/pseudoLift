class Pair:
	l = None
	r = None
	def __init__(self, left, right):
		self.l = left
		self.r = right
	def __repr__(self):
		return "("+str(self.l)+", "+str(self.r)+")"

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

