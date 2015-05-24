class Request:
	isInternalRequest = None #Internal/External
	clickedButtons = []   

	''' if internal ''' 
	whichElevator = None #0 , 1
	# clickedButtons = {9(7th), 8,7,6,5,4, 3(1th),2(CLOSED),1(OPENED), 0(None)}
	''' if external '''
	whichFloor = None # 1,2,3,4,5,6,7
	# clickedButtons = {2(down),1(up), 0(None)}
	def __init__(self, isInternalRequest, aux, clickedButtons):
		self.isInternalRequest = isInternalRequest
		self.clickedButtons = clickedButtons
		if (isInternalRequest):
			self.whichElevator = aux
			for i in range(len(clickedButtons)):
				print " IN: clicked btn "+str(clickedButtons[i]) +"\
				 in elevator "+str(self.whichElevator)
		else :
			self.whichFloor = aux
			for i in range(len(clickedButtons)):
				print " EX: clicked btn "+str(clickedButtons[i]) +"\
				 in floor "+str(self.whichFloor)
