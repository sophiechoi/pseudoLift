import time
from elevatorController import E_controller
from f import rem, enqItemFreq, deqItemFreq, deleteItem

e_controller = E_controller(2, 7)
print "\n"

while(True):
	myStr = raw_input('Enter your input:')
	if len(myStr) > 1:
		print ">> handle input"
		# I 0 3
		# E 4 2
	else:
		print ">> update next status"
		print e_controller
	time.sleep(1)
