from adxl345 import ADXL345
import Adafruit_MCP4725
from time import sleep

adxl345 = ADXL345()
dac = Adafruit_MCP4725.MCP4725()


while True:    
	axes = adxl345.getAxes(True)
	dac.set_voltage(axes["x"])
	print "ADXL345 on address 0x%x:" % (adxl345.address)
	print "   x = %.3fG" % ( axes['x'] )
	print "   y = %.3fG" % ( axes['y'] )
	print "   z = %.3fG" % ( axes['z'] )
	print "-----------------------------"
	sleep(1)
