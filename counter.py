from myhdl import *

def counter(msb, lsb, cout, clk, reset, of_msb=5, of_lsb=9, base=10):
    '''
    msb: output - the most significant bit 
    lsb: output - the least significant bit 
    cout: output - a carry out when of_msb is reached
    clk: input - tick tock
    reset: input - active low
    of_msb: input - msb overflow 
    of_lsb: input - lsb overflow 
    ''' 

    @always_seq(clk.posedge, reset=reset)
    def countLogic():
        if ( (msb >= of_msb) and (lsb >= of_lsb) ):
            cout.next = 1
            msb.next = 0
            lsb.next = 0
        elif ( lsb >= (base - 1) ):
            cout.next = 0 
            lsb.next = 0
            msb.next = msb + 1
        else:
            cout.next = 0 
            lsb.next = lsb + 1

    return countLogic
