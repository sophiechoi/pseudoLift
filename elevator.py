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
	def insertDst(self, numFloor):
		pass
		#for i in range(len(destinations)):
		#	if numFloor<destinations
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


############# TEST MAIN() ##################

#elevator = Elevator(7)
#elevator.go(3)