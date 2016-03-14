from myhdl import *

encoding = {0x0: "0x40",
			0x1: "0x79",
			0x2: "0x24",
			0x3: "0x30",
			0x4: "0x19",
			0x5: "0x12",
			0x6: "0x02",
			0x7: "0x78",
			0x8: "0x00",
			0x9: "0x18",
			0xA: "0x08",
			0xB: "0x03",
			0xC: "0x46",
			0xD: "0x21",
			0xE: "0x06",
			0xF: "0x0E"}
			
code = [None] * 16
for key, val in encoding.items():
	if 0x0 <= key <= 0xF:
		code[int(key)] = int(val, 16)
code = tuple(code)
	
def hcd2led(led, hcd, clock):
	""" Hex Code to Seven Segment LED
	
	led: output - seven segment display
	hcd: input - hex code
	clock: input - clock
	"""
	
	@always(clock.posedge)
	def logic():
		led.next = code[int(hcd)]
	
	return logic