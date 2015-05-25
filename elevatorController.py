from elevator import Elevator
from request import Request 
import time 

# love this article: http://stackoverflow.com/questions/4915920/how-to-delete-an-item-in-a-list-if-it-exists-python
def remove(L, value):
  try:
    L.remove(value)
  except ValueError:
    pass

class E_controller:
	'''TODO'''
	waitingRequests = [] 
	#clk = None
	#rst = None
	n = None
	f = None
	# requests = [] #maybe NOT need
	elevators = []
	def __init__(self, n, f, ele=Elevator(f)):
		print "E_controller.__init__()"
		self.n = n # N-way elevator 
		self.f = f # num of floors 
		for i in range(n):
			self.elevators.append(ele)
		print ("num of floors: "+str(self.f))
		print ("num of elevators: " + str(len(self.elevators)))
	def __filterElevator(self, movingStatus):
		newElevators = []
		for i in range(len(self.elevators)):
			if self.elevators[i].movingStatus == movingStatus or self.elevators[i].movingStatus == 0:
				newElevators.append(self.elevators[i])
		return newElevators
	def __pickClosestElevator(self, elevators, whichFloor):
		closest = None
		minDistance = 10
		for i in range(len(elevators)):
			if abs(elevators[i].currFloor - whichFloor) < minDistance:
				minDistance = abs(elevators[i].currFloor - whichFloor)
				closest = elevators[i]
		return i
	'''TODO'''
	def pickElevator(self, whichFloor, upOrDownBtn):
		if upOrDownBtn == 1: #if UP btn 
			# filter movingUp or Staying elevators
			filteredElevators = self.__filterElevator(2)
			# if not, use movingDown elevators
			if not filteredElevators :
				filteredElevators = self.elevators
			self.__pickClosestElevator(filteredElevators, whichFloor)
		elif upOrDownBtn ==2: #if DOWN btn
			# filter movingDown or Staying elevators
			filteredElevators = self.__filterElevator(1)
			# if not, use movingUp elevators
			if not filteredElevators :
				filteredElevators = self.elevators
			self.__pickClosestElevator(filteredElevators, whichFloor)
		### WHAT ABOUT UNHANDLED_BTNS? leftovers..
		#elif down button
			#filter movingStatus == 1, closest
			#else, closest
		#elif up & down button
			#both 0,or each one movingStatus=2,1, then each one
			#if both movingStatus=2, closest(=?first) one UP, second one to DOWN
			#movingS
		pass
	def enqRequest(self, request):
		if request.isInternal : 
			i 	= request.whichElevator
			btn = request.btn
			e   = elevators[i]
			if (btn == 1 or btn == 2): #handle OPEN/CLOSE button
				if 	e.movingStatus==0:
					if   (e.isOpen==1 and btn==2):
						e.closeDoor()
					elif (e.isOpen==0 and btn==1):
						e.openDoor()
				else:
					pass
			else: #handle NUM_OF_FLOOR(1~7) button			 
				newStation = btn - 2
				if (newStation == currFloor):
					#ignore if same floor with currFloor
					pass
				elif newStation in e.upperStations.extend(e.lowerStations):
					#ignore if already in stationslist
					pass
				else:
					e.insertDst(btn)
		else :
			'''TODO'''
			'''handle UP/DOWN buttons '''
			''' put in LEFT OVERS '''
			''' If DONE, remove from LEFT_OVER list'''
			waitingRequests.append(request)
			ii = request.whichFloor
			ee = self.pickElevator(ii, btn)
			request.chosenElevator(ee)
			ee.insertDst(btn)
	def updateOneClk(self):
		for i in range(len(self.elevators)):
			self.elevators[i].updateOneClk()
		print "status: "
		time.sleep(1)


############# MAIN() ##################
#e_controller = E_controller(2, 7)
e_controller = E_controller(1, 7, Elevator(7, 0, 2, [2,4,6]))
request1_in = Request(True, 0, [9,8,1])
request2_ex = Request(False, 3, [1, 2])
#e_controller.enqRequest(request1_in)
#e_controller.enqRequest(request2_ex)
#e_controller.updateOneClk()


