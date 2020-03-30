from qr204 import QR204
from qiwi import QiwiDonate
from time import sleep_ms

import machine
import beep

qd = QiwiDonate('QIWI_DONATE_TOKEN')

def print_message():
    
    donate = qd.get_donate()
    
    if isinstance(donate, tuple):
        beep.play_mario()
        printer = QR204(machine.UART(1, 9600))
        
        printer.align('c')
        printer.bold_enbl()
        printer.write(str(donate[2]))
        printer.write(' рублей от ')
        printer.uline_enbl()
        printer.writeln(donate[0])
        printer.uline_dsbl()
        printer.bold_dsbl()
        printer.align('<')
        
        printer.newline(2)
        printer.write(donate[1])
        printer.newline()
        printer.write('_' * 32)
        printer.newline()
        printer.sleep()

beep.play_beep()
while sta_if.isconnected():
    print_message()
    sleep_ms(3000)
    machine.lightsleep(10000)

sleep_ms(1000)
machine.reset()