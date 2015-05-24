class Request:
	isInternalRequest = None #Internal/External
	clickedButtons = []   

	''' if internal ''' 
	whichElevator = None 
	# clickedButtons = {9(7층), 8,7,6,5,4, 3(1층),2(닫힘),1(열림), 0(None)}
	''' if external '''
	whichFloor = None
	# clickedButtons = {3(both),2(down),1(up), 0(None)}
	def __init__(self, isInternalRequest, aux, clickedButtons):
		self.isInternalRequest = isInternalRequest
		if (isInternalRequest):
			self.whichElevator = aux
		else self.whichFloor = aux
		self.clickedButtons = clickedButtons