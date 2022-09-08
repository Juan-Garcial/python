import time

import pyvisa

rm = pyvisa.ResourceManager()
"""
source_2 = rm.open_resource('GPIB0::20::INSTR')
#print(inst.query("*IDN?"))

source_1 = rm.open_resource('GPIB0::19::INSTR')
source_1.write('VOLT:LEV 9')
source_2.write('VOLT:LEV 6')
"""

W_gen_1 = rm.open_resource('TCPIP0::10.0.7.161::inst0::INSTR')
print(W_gen_1.query("*IDN?"))
#W_gen_1.write('SOURce1:FREQ 200 ') # set frecuency
#W_gen_1.write('SOURce1:VOLTage 2') #set voltage
#W_gen_1.write('SOURce1:VOLTage:OFFset .1') # voltage offset