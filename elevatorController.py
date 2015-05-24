from elevator import Elevator

class E_controller:
	#clk = None
	#rst = None
	#status = None
	n = None
	f = None
	#internal_inputs = []
	#external_inputs = []
	requests = [] #maybe NOT need
	elevators = []
	def __init__(self, n, f):
		print "E_controller.__init__()"
		self.n = n # N-way elevator 
		self.f = f # num of floors 
		for i in range(n):
			self.elevators.append(Elevator(f))
		#for i in range(f):
		#	self.internal_inputs.append(0)
		#	print self.internal_inputs[i]
		#print ("num of floors: " + str(len(self.internal_inputs)))
		print ("num of floors: "+str(self.f))
		print ("num of elevators: " + str(len(self.elevators)))
	def requestScheduler():
		pass # while(True): doOneRequest, if end, take another interrupt
	def chooseOneRequest():
		pass
	def chooseOneElavator():
		pass
	def interruptWithRequest():
		pass


###############################
e_controller = E_controller(2, 7)
#elevator = Elevator(7)
