import time
from elevatorController import E_controller
from f import rem, enqItemFreq, deqItemFreq, deleteItem, parseAndGenRequest

e_controller = E_controller(2, 7)
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
		e_controller.enqRequest(r)
		print e_controller
	else:
		print ">> update next status"
		print e_controller
		e_controller.updateOneClk()
		print e_controller
		time.sleep(1)