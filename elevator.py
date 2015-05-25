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
	upperStations = None
	lowerStations = None
	def __init__(self, maxFloor=7, isOpen=0, movingStatus=0, upperStations=[], curFloor = 1):
		print "Elevator.init()"
		self.curFloor = curFloor
		self.maxFloor = maxFloor
		self.movingStatus = movingStatus
		self.isOpen = isOpen
		self.upperStations = {}
		self.lowerStations = {}
		for i in range(len(upperStations)):
			enqItemFreq(self.upperStations, upperStations[i])
	def __repr__(self):
		return "ELEVATOR STATE("+"curFloor: "+str(self.curFloor)+", isOpen: "+str(self.isOpen)+", movingStatus: "+str(self.movingStatus)+")\n"
	def __str__(self):
		return "ELEVATOR STATE("+"curFloor: "+str(self.curFloor)+", isOpen: "+str(self.isOpen)+", movingStatus: "+str(self.movingStatus)+")\n"
	def __printPos(self):
		print ">> "+str(self.curFloor) + " th floor"
	def __printStations(self, msg):
		if self.movingStatus==sMoving.UP:
			print msg+str(self.upperStations)+"/"+str(self.lowerStations)
		elif self.movingStatus==sMoving.DOWN:
			print msg+str(self.lowerStations)+"/"+str(self.upperStations)
	def __moveOneUp(self):
		if (self.curFloor < self.maxFloor):
			self.curFloor += 1
			print ".. moving up .. to "+str(self.curFloor)
	def __moveOneDown(self):
		if (self.curFloor > 1):
			self.curFloor -= 1
			print ".. moving down ..to "+str(self.curFloor)
	def __checkAndGoOneUp(self):
		ups = self.upperStations
		self.movingStatus = sMoving.UP
		sortedList = []
		for key in sorted(ups.iterkeys()):
			sortedList.append(key)
		dst = sortedList[0]
		if (dst == self.curFloor):
			deleteItem(ups, dst)
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
			deleteItem(lws, dst)
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

	def insertDst(self, newFloor):
		#print "insertDst()"
		self.__printStations(".. before: ")
		if newFloor > self.curFloor:
			if self.movingStatus==sMoving.STAY: #need?
				self.movingStatus =sMoving.UP #need?
			print ".. added upperStation .."
			enqItemFreq(self.upperStations, newFloor)
		elif newFloor < self.curFloor:
			if self.movingStatus==sMoving.STAY: #need?
				self.movingStatus =sMoving.DOWN #need?
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

############# TEST MAIN() ##################

#elevator = Elevator(7)
#elevator.go(3)
#print "----"
#e = Elevator(7, 0, 2, [3,4,6], 2)
#e.insertDst(3)
#e.insertDst(1)


