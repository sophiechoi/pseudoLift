class Elevator:
	isOpen = 0	# 0: closed, 1: opened
	movingStatus = 0 # 0: stay, 1: down, 2: up 
	curFloor = None 
	maxFloor = None
	destinations = [] #stop and Open
	def __init__(self, maxFloor):
		self.curFloor = 1
		self.maxFloor = maxFloor
		print "Elevator() init"
	def printPos(self):
		print ">> "+str(self.curFloor) + " th floor"
	def moveOneUp(self):
		if (self.curFloor < self.maxFloor):
			self.curFloor += 1
			print ".. moving up .."
	def moveOneDown(self):
		if (self.curFloor > 1):
			self.curFloor -= 1
			print ".. moving down .."
	def moveUp(self, n):
		self.printPos()
		for i in range(n):
			self.moveOneUp()
			self.printPos()
	def moveDown(self, n):
		self.printPos()
		for i in range(n):
			self.moveOneDown()
			self.printPos()
	def startMoving(self, dstFloor):
		if (dstFloor > self.curFloor):
			self.movingStatus = 2
			self.moveUp(dstFloor - self.curFloor)
		elif (dstFloor < self.curFloor):
			self.movingStatus = 1
			self.moveDown(self.curFloor - dstFloor)
	def endMoving(self):
		self.movingStatus = 0
		self.openDoor()
		self.closeDoor()		
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

#elevator = Elevator(7)
#elevator.go(3)