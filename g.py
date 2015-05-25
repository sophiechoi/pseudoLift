def enum(**named_values):
	return type('Enum', (), named_values)

Color = enum(a1=3, RED=1, YELLOW=2)
#print "color"
#print Color.RED
#print Color.RED ==1
#print Color.a1
