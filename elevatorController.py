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
			
			'''handle 1~7 FLOOR buttons''' # elevator is picked already!
			if e.movingStatus == 2:
				higherFloors = [] '''TODO'''#filter higher than currFloor
				lowerFloors = [] '''TODO'''#filter lower than currFloor
				for j in range(len(higherFloors)): 
					e.insertDst(higherFloors[j]) '''TODO: debug insertDst '''
				e.extendDst(lowerFloors)
					
		else :
			'''handle UP/DOWN buttons '''
			# e = self.pickElevator()
			pass
	def updateOneClk(self):
		'''TODO'''
		for i in range(len(self.elevators)):
			self.elevators[i].updateOneClk()
		time.sleep(1)


############# MAIN() ##################
#e_controller = E_controller(2, 7)
e_controller = E_controller(1, 7, Elevator(7, 0, 2, [3,4,5]))
request1_in = Request(True, 0, [9,8,1])
request2_ex = Request(False, 3, [1, 2])
print [1, 2, 3]
a = [1, 2, 3]
print a
a.remove(3)
remove(a,4)
print a
x = [4, 10,2,3 , 'a']
x.sort()
print x
#e_controller.enqRequest(request1_in)
#e_controller.enqRequest(request2_ex)
#e_controller.updateOneClk()

h = [1,2,3,4]
x = h
x.remove(3)
print h
print x

