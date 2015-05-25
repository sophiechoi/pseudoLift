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
	def pickElevator(self):
		#if up button
			#movingStatus == 2인 중에, 나랑 제일 가까운 것.
			#없으면, 그외중 가까운것
		#elif down button
			#movingStatus == 1인 중에, 나랑 제일 가까운 것.
			#없으면, 그외중 가까운것
		#elif up & down button
			#둘다 0이거나, movingStatus=2,1이 각각 하나씩 있으면, 각각 하나씩 
			#movingStatus=2만 있으면, 먼저 올라오는애를 up에, 나중을 down에
			#movingS
		pass
	def enqRequest(self, request):
		if request.isInternal : 
			''' handle OPEN/CLOSE buttons '''
			# OPEN/CLOSE buttons are only effective when elevators are STOPPED.
			i 	 = request.whichElevator
			btns = request.clickedButtons
			e    = elevators[i]
			if e.movingStatus==0 : 
				if (e.isOpen==1 and btns.contains(2)):
					e.closeDoor()
				elif (e.isOpen==0 and btns.contains(1)):
					e.openDoor()
			remove(btns, 1)
			remove(btns, 2)
			'''ignore if same floor with currFloor & ignore already in stationslist'''
			
			'''handle 1~7 FLOOR buttons''' # elevator is picked already!
			if e.movingStatus == 2 or movingStatus == 1:
				for j in range(len(btns)): 
					e.insertDst(btns[j])
			elif e.movingStatus == 0:
				pass					
		else :
			'''handle UP/DOWN buttons '''
			# ee = self.pickElevator()
			#	for j in range(len(btns)): 
			#		e.insertDst(btns[j])
			pass
	def updateOneClk(self):
		'''TODO'''
		for i in range(len(self.elevators)):
			self.elevators[i].updateOneClk()
		time.sleep(1)


############# MAIN() ##################
#e_controller = E_controller(2, 7)
e_controller = E_controller(1, 7, Elevator(7, 0, 2, [2,4,6]))
request1_in = Request(True, 0, [9,8,1])
request2_ex = Request(False, 3, [1, 2])
#e_controller.enqRequest(request1_in)
#e_controller.enqRequest(request2_ex)
#e_controller.updateOneClk()


