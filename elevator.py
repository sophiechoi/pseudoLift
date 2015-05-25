def remove(L, value):
  try:
    L.remove(value)
  except ValueError:
    pass

class Elevator:
	isOpen = None	# 0: closed, 1: opened
	movingStatus = None # 0: stay, 1: down, 2: up 
	curFloor = None 
	maxFloor = None
	upperStations = None
	lowerStations = None
	def __init__(self, maxFloor, isOpen=0, movingStatus=0, upperStations=[], curFloor = 1):
		self.curFloor = curFloor
		self.maxFloor = maxFloor
		self.movingStatus = movingStatus
		self.isOpen = isOpen
		self.upperStations = upperStations
		self.lowerStations = []
		print "Elevator.init() "+str(isOpen)+", "+ str(movingStatus)
		#self.printStations("init: ")
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
			self.movingStatus = 2
			self.__moveUp(dstFloor - self.curFloor)
		elif (dstFloor < self.curFloor):
			self.movingStatus = 1
			self.__moveDown(self.curFloor - dstFloor)
	def __endMoving(self):
		self.movingStatus = 0
		self.openDoor()
		self.closeDoor()
	def __insertInUpperStations(self, newFloor):
		stations = self.upperStations
		if not stations :
			stations.append(newFloor) 
		elif newFloor in stations:
			pass
		else:
			for i in range(len(stations)):
				if newFloor < stations[i] :
					stations.insert(i, newFloor)
					break
				elif i == (len(stations)-1):
					stations.append(newFloor)
	def __insertInLowerStations(self, newFloor):
		stations = self.lowerStations
		if not stations :
			stations.append(newFloor) 
		elif newFloor in stations:
			pass
		else:
			for i in range(len(stations)):
				if newFloor > stations[i] :
					stations.insert(i, newFloor)
					break
				elif i == (len(stations)-1):
					stations.append(newFloor)
	def __printStations(self, isBefore):
		if self.movingStatus==2:
			print isBefore+str(self.upperStations)+"/"+str(self.lowerStations)
		elif self.movingStatus==1:
			print isBefore+str(self.lowerStations)+"/"+str(self.upperStations)
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
	def cancelDst(self, oldFloor):
		'''TODO: cancel external dst '''
		remove(self.upperStations, oldFloor)
		remove(self.lowerStations, oldFloor)
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
	def updateOneClk(self): # do one thing = open/close/move one-floor up or down
		#if movingStatus == 0 :
		#	if 
		# if upperStations + lowerStations == []:
		#	movingStatus = 0
		pass
		#if destinations:

############# TEST MAIN() ##################

#elevator = Elevator(7)
#elevator.go(3)
#print "----"
#e = Elevator(7, 0, 2, [3,4,6], 2)
#e.insertDst(3)
#e.insertDst(1)
E= 1
print E
e= 2
print e
print E
