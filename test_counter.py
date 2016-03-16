from myhdl import *
from counter import *

ACTIVE_LOW, INACTIVE_HIGH = 0, 1

def testBench():
    msb, lsb, cout, clk, reset = [Signal(intbv(0)) for i in range(5)]
    reset = ResetSignal(0, active=ACTIVE_LOW, async=True)

    counter_1 = counter(msb, lsb, cout, clk, reset, of_msb=5, of_lsb=9)

    HALF_PERIOD = delay(10)

    @always(HALF_PERIOD)
    def clockGen():
        clk.next = not clk

    @instance
    def stimulus():
        reset.next = ACTIVE_LOW
        yield clk.negedge
        reset.next = INACTIVE_HIGH
        yield delay(2000)
        raise StopSimulation

    @instance
    def monitor():
        print("1 2 3 A HA HA")
        yield reset.posedge
        while 1:
            print(" %s%s    %s" % (msb, lsb, cout))
            yield clk.posedge
            yield delay(1)

    return clockGen, stimulus, monitor, counter_1

tb = testBench()
Simulation(tb).run()
