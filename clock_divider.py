from myhdl import *

def clockDivider(clk_in, clk_out, reset, division = 1):
    '''
    clk_in: input - the input clock of arbitrary frequency
    clk_out: output - output clock of desired frequency
    division: input - what number to divide the clock by
    '''

    #div_count = Signal(modbv(0, min=0, max=26))
    div_count = Signal(intbv(0)[26:])
    
    @always_seq(clk_in.posedge, reset=reset)
    def clockDiv():
        if (div_count >= division-1):
            clk_out.next = not clk_out
            div_count.next = 0
        else:
            div_count.next = div_count + 1

    return clockDiv
