class Request:
	isInternal = None #True: Internal, FalseExternal
	#btn = [] ###btons >> ONE btn  
	btn = None
	''' if internal ''' 
	whichElevator = None #0 , 1 , .. (N-1)
	# btn = {9(7th), 8,7,6,5,4, 3(1th),2(CLOSED),1(OPENED), 0(None??)}

	''' if external '''
	whichFloor = None # 1,2,3,4,5,6,7, .. F
	# btn = {2(down),1(up), 0(None??)}
	chosenElevator = None
	def __init__(self, isInternal, aux, btn):
		self.isInternal = isInternal
		if (isInternal):
			self.whichElevator = aux
			print " IN: clicked btn "+str(btn) +" in elevator "+str(self.whichElevator)
		else :
			self.whichFloor = aux
			print " EX: clicked btn "+str(btn) +" in floor "+str(self.whichFloor)

