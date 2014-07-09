from __future__ import division

def cel_to_fahren(temp):
	print "%d C = %d F" %(temp,((9/5) * temp + 32))

def fahren_to_cel(temp):
	print "%d F = %d C" %(temp,((5/9) * (temp - 32)))


print "Temperature Converter"
temp = int(raw_input("Enter a temperature:"))
unit = raw_input ("Convert to (F)ahrenheit or (C)elcius?")
	
if unit == "C":
	fahren_to_cel(temp)
else:
	cel_to_fahren(temp)
			
