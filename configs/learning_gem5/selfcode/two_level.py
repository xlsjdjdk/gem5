# The first step is to import the SimObjects we are going to extend.
import m5
from m5.objects import *
from caches import *
import os

#######################################
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--bin", help="The executable file name. Default: test.\
                It should be under tests/test-progs/selftest/$isa/bin/.")
parser.add_option("--clk", help="CPU clk. Default: 1GHz.")
parser.add_option("--cache_block", help="CPU cache block. Default: 64.")
parser.add_option("--l1i_size", help="L1 icache size. Default: 16kB.")
parser.add_option("--l1d_size", help="L1 dcache size. Default: 64kB.")
parser.add_option("--l2_size", help="L2 cache size. Default: 256kB.")
parser.add_option("--mem_size", help ="DRAM size. Default: 512MB.")
parser.add_option("--cpu_model", help ="CPU type. Default: TimingSimpleCPU")


(options, args) = parser.parse_args()
#######################################

system = System()

system.clk_domain = SrcClockDomain()
if not options or not options.clk:
    system.clk_domain.clock = '1GHz'
else:
    system.clk_domain.clock = options.clk

system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
if not options or not options.mem_size:
    system.mem_ranges = [AddrRange('512MB')]
else:
    system.mem_ranges = [AddrRange(options.mem_size)]

if not options or not options.cpu_model:
    system.cpu = TimingSimpleCPU()
else:
    try:
        system.cpu = eval(options.cpu_model+'()')
    except ValueError:
        print("Invalid CPU model type!")

system.cpu.icache = L1ICache(options)
system.cpu.dcache = L1DCache(options)

system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

# The L2 bus msut be created to connect L1 Cache with L2 Cache!
system.l2bus = L2XBar()
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

system.l2cache = L2Cache()
system.l2cache.connectCPUSideBus(system.l2bus)
system.membus = SystemXBar()
system.l2cache.connectMemSideBus(system.membus)

if not options or not options.cache_block:
    system.cache_line_size = 64
else:
    system.cache_line_size = options.cache_block

system.cpu.createInterruptController()
if m5.defines.buildEnv['TARGET_ISA'] == "x86":
    system.cpu.interrupts[0].pio = system.membus.mem_side_ports
    system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
    system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# Now we have finished instantiating system.

# Let's set the CPU workload.

# get ISA for the binary to run.
isa = str(m5.defines.buildEnv['TARGET_ISA']).lower()

# Default to running 'test', use the compiled ISA to find the binary
thispath = os.path.dirname(os.path.realpath(__file__))
if not options or not options.bin:
    bin_name = 'test'
else:
    bin_name = options.bin

binary = os.path.join(thispath, '../../../',
                'tests/test-progs/selftest/bin/', isa, bin_name)
system.workload = SEWorkload.init_compatible(binary)

# Create the process to run out CPU.
process = Process()
process.cmd = [binary]
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system = False, system = system)
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick %i because %s'\
                % (m5.curTick(), exit_event.getCause()))