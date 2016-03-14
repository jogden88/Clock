from random import randrange
from seven_segment import *
#from seven_segment import bcd2led
from myhdl import *

PERIOD = 10

def bench():

	led = Signal(intbv(0)[7:])
	hcd = Signal(intbv(0)[4:])
	clock = Signal(bool(0))
	
	dut = hcd2led(led, hcd, clock)
	
	@always(delay(PERIOD//2))
	def clkgen():
		clock.next = not clock
		
	@instance
	def check():
		for i in range(256):
			hcd.next = randrange(16)
			yield clock.posedge
			yield clock.negedge
			expected = int(encoding[int(hcd)], 16)
			assert led == expected
		raise StopSimulation
		
	return dut, clkgen, check
	
def test_bench():
	sim = Simulation(bench())
	sim.run()