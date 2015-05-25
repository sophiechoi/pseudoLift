import time
from elevatorController import E_controller
from f import rem, enqItemFreq, deqItemFreq, deleteItem, parseAndGenRequest

e_controller = E_controller(2, 7)

print "\n"
print "--------------------------------------"
print "-----------------MANUAL---------------"
print "inputType1: I 0~2(whichElevator) 1~9(internalBtns, 1: close, 2: open, 3~9: 1F~7F)"
print "ex>> I 0 5"
print "inputType2: E 1~7(whichFloor) 1~2(1: down, 2: up)"
print "ex>> E 6 1"
print "inpuTtype3: just [Enter], to continue next state"
print "ex>> [Enter]"
print "--------------------------------------"
print "--------------------------------------"
print "\n"
print "\n"

while(True):
	userInput = raw_input('Enter your input:')
	if len(userInput) > 1:
		print ">> handle input"
		# userInput ex) I 0 2 (open )
		# userInput ex) I 0 5 (go 3th floor)
		# userInput ex) E 6 1 (6th floor, down btn)
		r = parseAndGenRequest(userInput)
		print "> "+str(r)
		print "x0: "+str(len(e_controller.elevators[0].upperStations))
		print "x1: "+str(len(e_controller.elevators[1].upperStations))
		e_controller.enqRequest(r)
		print "x0: "+str(len(e_controller.elevators[0].upperStations))
		print "x1: "+str(len(e_controller.elevators[1].upperStations))
		print e_controller
	else:
		print ">> update next status"
		#print "0: "+str(e_controller.elevators[0])
		#print "1: "+str(e_controller.elevators[0])
		print e_controller
		e_controller.updateOneClk()
		#print "0: "+str(e_controller.elevators[0])
		#print "1: "+str(e_controller.elevators[0])
		print e_controller
		time.sleep(1)