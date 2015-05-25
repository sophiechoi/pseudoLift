from f import rem, enqItemFreq, deqItemFreq, deleteItem

class Elevator:
	isOpen = None	# 0: closed, 1: opened
	movingStatus = None # 0: stay, 1: down, 2: up 
	curFloor = None  # 1,2, ~ 7
	maxFloor = None
	upperStations = {}
	lowerStations = {}
	def __init__(self, maxFloor, isOpen=0, movingStatus=0, upperStations=[], curFloor = 1):
		self.curFloor = curFloor
		self.maxFloor = maxFloor
		self.movingStatus = movingStatus
		self.isOpen = isOpen
		for i in range(len(upperStations)):
			enqItemFreq(self.upperStations, upperStations[i])
		print "Elevator.init() "+str(isOpen)+", "+ str(movingStatus)
		#self.printStations("init: ")
	def __repr__(self):
		return "ELEVATOR STATE("+"curFloor: "+str(self.curFloor)+", isOpen: "+str(self.isOpen)+", movingStatus: "+str(self.movingStatus)+")\n"
	def __str__(self):
		return "ELEVATOR STATE("+"curFloor: "+str(self.curFloor)+", isOpen: "+str(self.isOpen)+", movingStatus: "+str(self.movingStatus)+")\n"
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
		self.__printPos()
		for i in range(n):
			self.__moveOneUp()
			self.__printPos()
	def __moveDown(self, n):
		self.__printPos()
		for i in range(n):
			self.moveOneDown()
			self.__printPos()
	def __startMoving(self, dstFloor):
		if (dstFloor > self.curFloor):
			self.movingStatus = 2 #up
			self.__moveUp(dstFloor - self.curFloor)
		elif (dstFloor < self.curFloor):
			self.movingStatus = 1 #down
			self.__moveDown(self.curFloor - dstFloor)
	def __endMoving(self):
		self.movingStatus = 0 #stay
		self.openDoor()
		self.closeDoor()
	def __printStations(self, isBefore):
		if self.movingStatus==2:
			print isBefore+str(self.upperStations)+"/"+str(self.lowerStations)
		elif self.movingStatus==1:
			print isBefore+str(self.lowerStations)+"/"+str(self.upperStations)
	def __insertInUpperStations(self, newFloor):
		enqItemFreq(self.upperStations, newFloor)
	def __insertInLowerStations(self, newFloor):
		enqItemFreq(self.lowerStations, newFloor)
	def insertDst(self, newFloor):
		self.__printStations("before: ")
		print str(self.movingStatus)
		if newFloor > self.curFloor:
			print "upper"
			self.__insertInUpperStations(newFloor)
		elif newFloor < self.curFloor:
			print "lower"
			self.__insertInLowerStations(newFloor)
		self.__printStations("after: ")
	def openDoor(self):
		isOpen = 1
		print ".. door opened .."
	def closeDoor(self):
		isOpen = 0
		print ".. door closed .."
	def go(self, dstFloor):
		print ".. start from "+str(self.curFloor) + " th floor .."
		self.__startMoving(dstFloor)
		self.__endMoving()
	def moveOneStepUp(self):
		pass
	def updateOneClk(self): # do one thing = open/close/move one-floor up or down
		'''TODO'''

		if self.movingStatus == 0 :
			if len(self.upperStations)>0 and len(self.lowerStations)==0:
				self.movingStatus = 2 #up
				sortedList = []
				for key in sorted(self.upperStations.iterkeys()):
					sortedList.append(key)
				dst = sortedList[0]
				if (dst > self.curFloor):
					self.__moveOneUp()
				elif (dst == self.curFloor): # or CONTAINS?
					removeItem(self.upperStations, dst)
					self.openDoor()
			elif len(self.upperStations)==0 and len(self.lowerStations)>0:
				self.movingStatus = 1
		else:
			if len(self.upperStations)==0 and len(self.lowerStations)==0:
				self.movingStatus = 0
			else: 
				pass

############# TEST MAIN() ##################

#elevator = Elevator(7)
#elevator.go(3)
#print "----"
#e = Elevator(7, 0, 2, [3,4,6], 2)
#e.insertDst(3)
#e.insertDst(1)


