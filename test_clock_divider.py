from myhdl import *
from clock_divider import *

def testBench():
    clk_in, clk_out = [Signal(intbv(0)) for i in range(2)]

    reset = ResetSignal(1, active = 0, async = True)

    clock_div = clockDivider(clk_in, clk_out, reset, division = 50)

    HALF_PERIOD = delay(1)

    @always(HALF_PERIOD)
    def clockGen():
        clk_in.next = not clk_in

    @instance
    def stimulus():
        yield delay(500)
        raise StopSimulation
        
    @instance
    def monitor():
        print("Clock Divider Test")
        print("In  Out")
        while True:
            yield clk_in.negedge
            print("%s   %s" % (int(clk_in), clk_out))
            yield clk_in.posedge
            print("%s   %s" % (int(clk_in), clk_out))

    return clock_div, clockGen, stimulus, monitor

tb = testBench()
Simulation(tb).run()
