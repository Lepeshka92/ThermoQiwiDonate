from machine import PWM, Pin
from time import sleep_ms
BEEP_PIN = 4
NOTE_C  = 523
NOTE_CS = 554
NOTE_D  = 587
NOTE_DS = 622
NOTE_E  = 659
NOTE_F  = 698
NOTE_FS = 740
NOTE_G  = 784
NOTE_GS = 831
NOTE_A  = 880
NOTE_AS = 932
NOTE_B  = 988


def play_beep(n=NOTE_C, d=100):
    beeper = PWM(Pin(BEEP_PIN, Pin.OUT), freq=n, duty=512)
    sleep_ms(d)
    beeper.deinit()
    
def play_mario():
    lst = [(NOTE_E, 70, 100),
           (NOTE_E, 70, 300),
           (NOTE_E, 70, 300),
           (NOTE_C, 70, 100),
           (NOTE_E, 70, 300),
           (NOTE_G, 70, 550)]
    for s in lst:
        play_beep(s[0], s[1])
        sleep_ms(s[2])