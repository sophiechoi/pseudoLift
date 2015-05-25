class Request:
	isInternal = None #True: Internal, FalseExternal
	#btn = [] ###btons >> ONE btn  
	btn = None
	''' if internal ''' 
	which = None
	#whichElevator = None #0 , 1 , .. (N-1)
	# btn = {9(7th), 8,7,6,5,4, 3(1th),2(OPENED),1(CLOSED), 0(None??)}

	''' if external '''
	#whichFloor = None # 1,2,3,4,5,6,7, .. F
	# btn = {2(up),1(down), 0(None??)}
	chosenElevator = None
	def __init__(self, isInternal, aux, btn):
		self.isInternal = isInternal
		self.which = aux
		if (isInternal):
			print " IN: clicked btn "+str(btn) +" in elevator "+str(self.whichElevator)
		else :
			print " EX: clicked btn "+str(btn) +" in floor "+str(self.whichFloor)
	def __repr__(self):
		if self.isInternal:
			return "Request("+str(self.isInternal) +", "+str(self.whichElevator)+", "+str(self.btn)+")"
		else :
			return "Request("+str(self.isInternal) +", "+str(self.whichFloor)+", "+str(self.btn)+", "+str(self.chosenElevator)+")"		

r1 = Request(True, 1, 3)
r2 = Request(False, 2, 4)
r3 = Request(True, 1, 3)
l = [r1, r2, r3]
#print l
if Request(True, 1, 3) in l:
	print "is"
else: 
	print "not"

if r1 in l:
	print "is2"

l2 = [x for x in l if x.isInternal==True and x.whichElevator ==1]
print l2