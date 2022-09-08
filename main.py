import time

import pyvisa

rm = pyvisa.ResourceManager()
source_2 = rm.open_resource('GPIB0::20::INSTR')
#print(inst.query("*IDN?"))

source_1 = rm.open_resource('GPIB0::19::INSTR')
source_1.write('VOLT:LEV 9')
source_2.write('VOLT:LEV 6')
