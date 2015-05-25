import time
from elevatorController import E_Controller

#elevatorController = E_Controller

while(True):
	myStr = raw_input('Enter your input:')
	if len(myStr) > 1:
		print "handle input"
	else:
		print "update next status"
	time.sleep(1)
