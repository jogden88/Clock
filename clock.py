from myhdl import *
from counter import *
from seven_segment import *
from clock_divider import *

def myClock(hrs_tens_led, hrs_ones_led, min_tens_led, min_ones_led, \
            sec_tens_led, sec_ones_led, sys_clk, reset):

    ''' 24 Hour Clock HH:MM:SS
    
    OUTPUTS
    ===
    hrs_tens, hrs_ones : Hours 7 segmend LEDs
    min_tens, hrs_ones : Minutes 7 segmend LEDs
    sec_tens, hrs_ones : Seconds 7 segmend LEDs
    
    INPUTS
    ===
    sys_clock : 50 Mhz from Altera DE1-SoC/DE2
    reset : Reset !
    '''

    hrs_tens, hrs_ones, min_tens, \
        min_ones, sec_tens, sec_ones = [Signal(intbv(0)[4:]) for i in range(6)]

    sec_cout, min_cout, hrs_cout = [Signal(bool(0)) for i in range(3)]

    clk_1hz = Signal(bool(0))

    divided_clk = clockDivider(sys_clk, clk_1hz, reset, division = int(25e6))   

    seconds_clock = counter(sec_tens, sec_ones, sec_cout, clk_1hz, reset, 1, 5) 
    minutes_clock = counter(min_tens, min_ones, min_cout, sec_cout, reset, 1, 5) 
    hours_clock = counter(hrs_tens, hrs_ones, hrs_cout, min_cout, reset, 2, 4) 

    sec_ones_hcd = hcd2led(sec_ones_led, sec_ones, clk_1hz)
    sec_tens_hcd = hcd2led(sec_tens_led, sec_tens, clk_1hz)

    min_ones_hcd = hcd2led(min_ones_led, min_ones, clk_1hz)
    min_tens_hcd = hcd2led(min_tens_led, min_tens, clk_1hz)

    hrs_ones_hcd = hcd2led(hrs_ones_led, hrs_ones, clk_1hz)
    hrs_tens_hcd = hcd2led(hrs_tens_led, hrs_tens, clk_1hz)

    return divided_clk, seconds_clock, minutes_clock, hours_clock, \
        sec_ones_hcd, sec_tens_hcd, min_ones_hcd, min_tens_hcd, \
        hrs_ones_hcd, hrs_tens_hcd

def convert():
    hrs_tens_led, hrs_ones_led, min_tens_led, min_ones_led, \
            sec_tens_led, sec_ones_led = [Signal(intbv(0)[7:]) for i in range(6)]

    sys_clk = Signal(bool(0))
    reset = ResetSignal(0, active = 0, async = True)

    toVHDL(myClock, hrs_tens_led, hrs_ones_led, min_tens_led, min_ones_led, \
           sec_tens_led, sec_ones_led, sys_clk, reset)

convert()
