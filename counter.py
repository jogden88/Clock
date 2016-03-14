from myhdl import *

def Counter(count, cout, clk, reset, overflow=9):
    '''
    count: output - the count
    cout: output - a carry out
    clk: input - tick tock
    reset: input - active low
    overflow: input - where to overflow for cout
    ''' 

    @always_seq(clk.posedge, reset=reset)
    def countLogic():
        if (count >= overflow):
            cout.next = 1;
            count.next = 0; 
        else:
            cout.next = 0
            count.next = (count + 1)

    return countLogic
