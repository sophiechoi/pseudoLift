from elevator import Elevator
from request import Request 
import time 

class E_controller:
	#clk = None
	#rst = None
	n = None
	f = None
	# requests = [] #maybe NOT need
	elevators = []
	def __init__(self, n, f):
		print "E_controller.__init__()"
		self.n = n # N-way elevator 
		self.f = f # num of floors 
		for i in range(n):
			self.elevators.append(Elevator(f))
		print ("num of floors: "+str(self.f))
		print ("num of elevators: " + str(len(self.elevators)))
	def pickElevator(self):
		pass
	def enqRequest(self, request):# while(True): doOneRequest, if end, take another interrupt
		#e = self.pickElevator()
		pass
	def updateOneClk(self):
		for i in range(len(self.elevators)):
			self.elevators[i].updateOneClk()
		time.sleep(1)


############# MAIN() ##################
e_controller = E_controller(2, 7)
request1_in = Request(True, 0, [9,8,1])
request2_ex = Request(False, 3, [1, 2])
#e_controller.enqRequest(request1_in)
#e_controller.enqRequest(request2_ex)
#e_controller.updateOneClk()