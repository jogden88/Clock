from myhdl import *
from counter import *

ACTIVE_LOW, INACTIVE_HIGH = 0, 1

def testBench():
    count, cout, clk, reset = [Signal(intbv(0)) for i in range(4)]
    reset = ResetSignal(0, active=ACTIVE_LOW, async=True)

    counter_1 = counter(count, cout, clk, reset, overflow=9)

    HALF_PERIOD = delay(10)

    @always(HALF_PERIOD)
    def clockGen():
        clk.next = not clk

    @instance
    def stimulus():
        reset.next = ACTIVE_LOW
        yield clk.negedge
        reset.next = INACTIVE_HIGH
        yield delay(1000)
        raise StopSimulation

    @instance
    def monitor():
        print("1 2 3 A HA HA")
        yield reset.posedge
        while 1:
            print(" %s    %s" % (count, cout))
            yield clk.posedge
            yield delay(1)

    return clockGen, stimulus, monitor, counter_1

tb = testBench()
Simulation(tb).run()
