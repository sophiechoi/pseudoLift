from f import rem, enqItemFreq, deqItemFreq, deleteItem
from g import enum
import time 

#Status
sMoving = enum(STAY=0, DOWN=1, UP=2)
sOpen = enum(CLOSED=0, OPENED=1)
sFloor = enum(F1=1, F2=2, F3=3, F4=4, F5=5, F6=6, F7=7)

class Elevator:
	isOpen = None	
	movingStatus = None 
	curFloor = None
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
			self.movingStatus = sMoving.UP
			self.__moveUp(dstFloor - self.curFloor)
		elif (dstFloor < self.curFloor):
			self.movingStatus = sMoving.DOWN
			self.__moveDown(self.curFloor - dstFloor)
	def __endMoving(self):
		self.movingStatus = sMoving.STAY
		self.openDoor()
		self.closeDoor()
	def __printStations(self, msg):
		if self.movingStatus==sMoving.UP:
			print msg+str(self.upperStations)+"/"+str(self.lowerStations)
		elif self.movingStatus==sMoving.DOWN:
			print msg+str(self.lowerStations)+"/"+str(self.upperStations)
	def insertDst(self, newFloor):
		print "newFloor: "
		print newFloor
		self.__printStations(".. before: ")
		if newFloor > self.curFloor:
			if self.movingStatus==sMoving.STAY: #need?
				self.movingStatus =sMoving.UP
			print ".. added upperStation .."
			enqItemFreq(self.upperStations, newFloor)
		elif newFloor < self.curFloor:
			if self.movingStatus==sMoving.STAY: #need?
				self.movingStatus =sMoving.DOWN
			print ".. added lowerStation.."
			enqItemFreq(self.lowerStations, newFloor)
		self.__printStations(".. after: ")
	def openDoor(self):
		isOpen = sOpen.OPENED
		print ".. door opened .."
		time.sleep(1)
		self.closeDoor()
	def closeDoor(self):
		isOpen = sOpen.CLOSED
		print ".. door closed .."
	def go(self, dstFloor):
		print ".. start from "+str(self.curFloor) + " th floor .."
		self.__startMoving(dstFloor)
		#self.__endMoving()
	def __checkAndGoOneUp(self):
		ups = self.upperStations
		self.movingStatus = sMoving.UP
		sortedList = []
		for key in sorted(ups.iterkeys()):
			sortedList.append(key)
		dst = sortedList[0]
		if (dst == self.curFloor):
			removeItem(ups, dst)
			self.movingStatus = sMoving.STAY
			self.openDoor()
		elif len(ups)>0:
			self.__moveOneUp()
		else:
			self.movingStatus = sMoving.STAY
	def __checkAndGoOneDown(self):
		lws = self.lowerStations
		self.movingStatus = sMoving.DOWN
		sortedList = []
		for key in sorted(lws.iterkeys()):
			sortedList.append(key)
		dst = sortedList[-1]
		if (dst == self.curFloor):
			removeItem(lws, dst)
			self.movingStatus = sMoving.STAY
			self.openDoor()
		elif len(lws)>0:
			self.__moveOneDown()
		else:
			self.movingStatus = sMoving.STAY
	def updateOneClk(self): 
		ups = self.upperStations
		lws = self.lowerStations

		if len(ups)==0 and len(lws)==0:
			self.movingStatus = sMoving.STAY
		else:
			if self.movingStatus == sMoving.STAY :
				if len(ups)>0 and len(lws)==0:
					self.__checkAndGoOneUp()
				elif len(ups)==0 and len(lws)>0:
					self.__checkAndGoOneDown()
			elif self.movingStatus == sMoving.UP :
				self.__checkAndGoOneUp()
			elif self.movingStatus == sMoving.DOWN :
				self.__checkAndGoOneDown()

############# TEST MAIN() ##################

#elevator = Elevator(7)
#elevator.go(3)
#print "----"
#e = Elevator(7, 0, 2, [3,4,6], 2)
#e.insertDst(3)
#e.insertDst(1)


