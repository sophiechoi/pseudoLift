from g import enum

#Status
sInternal = enum(I=True, E=False)

class Request:
	isI = None
	whichN = None 
	btn = None

	''' if internal ''' 
	# wihchN = whichElevator = {0, 1, .. (N-1)}
	# btn = {9(7th), 8,7,6,5,4, 3(1th),2(OPENED),1(CLOSED), 0(None?)}

	''' if external '''
	# whichN = whichFloor = {1, 2, 3, 4, 5, 6, 7}
	# btn = {2(up),1(down), 0(None?)}

	chosenElevatorIndex = None  

	def __init__(self, isInternal, whichN, btn):
		self.isI = isInternal
		self.whichN = whichN
		self.btn = btn
	def __repr__(self):
		if self.isI:
			return "Req("+str(self.isI) +", "+str(self.whichN)+", "+str(self.btn)+")"
		else:
			return "Req("+str(self.isI) +", "+str(self.whichN)+", "+str(self.btn)+", "+str(self.chosenElevator)+")"
	def __str__(self):
		if self.isI:
			return " IN: clicked btn_"+str(self.btn) +" in elevator_"+str(self.whichN)
		else:
			return " EX: clicked btn_"+str(self.btn) +" in floor_"+str(self.whichN)