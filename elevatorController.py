from elevator import Elevator
from request import Request 
from pair import Pair
import time 
from f import rem, enqItemFreq, deqItemFreq, deleteItem
from g import enum

#Status
E_Btns  = enum(UP=2, DOWN=1)
I_Btns  = enum(NNONE=0, CLOSE=1, OPEN=2, F1=3, F2=4, F3=5, F4=6, F5=7, F6=8, F7=9)
sMoving = enum(STAY=0, DOWN=1, UP=2) #duplicated
sOpen = enum(CLOSED=0, OPENED=1) #duplicated

class E_controller:
	n = None
	f = None
	rst = None
	waitingRequests = [] 
	elevators = []

	def __init__(self, numElevators, numFloors=7, ele=Elevator(f)):
		print "E_controller.init()"
		self.n = numElevators
		self.f = numFloors 
		for i in range(numElevators):
			self.elevators.append(ele)
		print ("num of floors: "+str(self.f))
		print ("num of elevators: " + str(len(self.elevators)))

	def __repr__(self):
		result = ""
		for i in range(len(self.elevators)):
			result += str(self.elevators[i])
		return result

	def __filterElevator(self, movingStatus):
		newElevators = []
		for i in range(len(self.elevators)):
			if self.elevators[i].movingStatus == movingStatus or self.elevators[i].movingStatus == 0:
				newElevators.append(self.elevators[i])
		return newElevators

	def __pickClosestElevator(self, elevators, whichN):
		closest = None
		minDistance = len(self.elevators) + 1
		es = self.elevators
		for i in range(len(es)):
			if abs(es[i].curFloor - whichN) < minDistance:
				minDistance = abs(es[i].curFloor - whichN)
				closest = es[i]
		return i

	def __pickElevator(self, whichN, upOrDownBtn):
		if upOrDownBtn==E_Btns.UP: 
			filteredElevators = self.__filterElevator(sMoving.UP) #UP & STAY
			if not filteredElevators :
				filteredElevators = self.elevators
			return self.__pickClosestElevator(filteredElevators, whichN)

		elif upOrDownBtn==E_Btns.DOWN:
			filteredElevators = self.__filterElevator(sMoving.DOWN) #DOWN & STAY
			if not filteredElevators :
				filteredElevators = self.elevators
			return self.__pickClosestElevator(filteredElevators, whichN)

	def enqRequest(self, request):
		i 	= int(request.whichN)
		btn = int(request.btn)
		if request.isI : 
			e   = self.elevators[i]
			if (btn == I_Btns.OPEN or btn == I_Btns.CLOSE):
				if 	e.movingStatus==sMoving.STAY:
					if   (e.isOpen==sOpen.OPENED and btn==I_Btns.CLOSE):
						e.closeDoor()
					elif (e.isOpen==sOpen.CLOSED and btn==I_Btns.OPEN):
						e.openDoor()
				else:
					pass
			else: #handle NUM_OF_FLOOR(1~7) button			 
				newStation = btn - 2
				if (newStation == e.curFloor):
					#ignore if same floor with curFloor
					pass
				else:
					e.insertDst(newStation)
		else : # handle EXTERNAL UP/DOWN buttons
			self.waitingRequests.append(request)
			eIndex = self.__pickElevator(i, btn)
			e 	   = self.elevators[eIndex]
			request.chosenElevatorIndex = eIndex # INITIAL MARK 
			newStation = i
			e.insertDst(newStation)

	def enqRequests(self, requests):
		pass

	def updateOneClk(self):
		#If waitingRequest is achieved unintentionally, CANCEL it.
		pairs = [] #pair = (curFloors, movingStatus)
		es = self.elevators
		for i in range(len(es)):
			pair = Pair(es[i].curFloor, es[i].movingStatus)
			pairs.append(pair)
		for i in range(len(pairs)):
			achieved = [r for r in self.waitingRequests if r.isI==False and r.whichN==pairs[i].l and x.btn==pairs[i].r]
			for a in range(len(achieved)):
				a.chosenElevator.deqItemFreq(paris.l)
				self.waitingRequests.remove(a)
		#IF REQUESTs EXIST, handle them

		#UPDATE TO NEXT STATUS(FLOOR)		
		for i in range(len(es)):
			es[i].updateOneClk()
		print "[[[ELEVETOR STATES]]]"
		for i in range(len(es)):
			print es[i]
		time.sleep(1)





############# MAIN() ##################
#e_controller = E_controller(2, 7)
#e_controller = E_controller(1, 7, Elevator(7, 0, 2, [2,4,6]))
#request1_in = Request(True, 0, [9,8,1])
#request2_ex = Request(False, 3, [1, 2])
#e_controller.enqRequest(request1_in)
#e_controller.enqRequest(request2_ex)
#e_controller.updateOneClk()


