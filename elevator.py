class Elevator:
	isOpen = None	# 0: closed, 1: opened
	movingStatus = None # 0: stay, 1: down, 2: up 
	curFloor = None 
	maxFloor = None
	destinations = None #stop by and open #>> STATIONS
	def __init__(self, maxFloor, isOpen=0, movingStatus=0, destinations=[]):
		self.curFloor = 1
		self.maxFloor = maxFloor
		self.movingStatus = movingStatus
		self.isOpen = isOpen
		self.destinations = destinations 
		print "Elevator.init() "+str(isOpen)+", "+ str(movingStatus)+", "+str(destinations)
	def __repr__(self):
		pass
	def __printPos(self):
		print ">> "+str(self.curFloor) + " th floor"
	def __moveOneUp(self):
		if (self.curFloor < self.maxFloor):
			self.curFloor += 1
			print ".. moving up .."
	def __moveOneDown(self):
		if (self.curFloor > 1):
			self.curFloor -= 1
			print ".. moving down .."
	def __moveUp(self, n):
		self.printPos()
		for i in range(n):
			self.moveOneUp()
			self.printPos()
	def __moveDown(self, n):
		self.printPos()
		for i in range(n):
			self.moveOneDown()
			self.printPos()
	def __startMoving(self, dstFloor):
		if (dstFloor > self.curFloor):
			self.movingStatus = 2
			self.moveUp(dstFloor - self.curFloor)
		elif (dstFloor < self.curFloor):
			self.movingStatus = 1
			self.moveDown(self.curFloor - dstFloor)
	def __endMoving(self):
		self.movingStatus = 0
		self.openDoor()
		self.closeDoor()
	def extendDst(self, floors):
		destinations.extend(floors)
	'''TODO'''
	'''TODO'''
	'''SHOULD DEBUG: 4,5,6,2,1 CAN OCCUR !!'''
	def insertDst(self, newFloor):
		print "insertDst, before: "+str(destinations)
		if not destinations:
			destinations.append(newFloor)
		else :
			if self.movingStatus == 1:
				for i in range(len(self.destinations)):
					if newFloor > self.destinations[i] :
						self.destinations.insert(i, newFloor)
						break
					elif i == (len(self.destinations)-1):
						dself.estinations.append(newFloor)
			elif self.movingStatus == 2: 
				for i in range(len(self.destinations)):
					if newFloor < self.destinations[i] :
						self.destinations.insert(i, newFloor)
						break
					elif i == (len(self.destinations)-1):
						self.destinations.append(newFloor)
		print "insertDst, after: "+str(destinations)
	def openDoor(self):
		isOpen = 1
		print ".. door opened .."
	def closeDoor(self):
		isOpen = 0
		print ".. door closed .."
	def go(self, dstFloor):
		print ".. start from "+str(self.curFloor) + " th floor .."
		self.startMoving(dstFloor)
		self.endMoving()
	def updateOneClk(self): # do one thing = open/close/move one-floor up or down
		pass
		#if destinations:

############# TEST MAIN() ##################

#elevator = Elevator(7)
#elevator.go(3)