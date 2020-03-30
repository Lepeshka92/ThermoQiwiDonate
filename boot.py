import gc
import network

aps = dict()
aps['WiFi1'] = 'Password1'
aps['WiFi2'] = 'Password2'
aps['WiFi3'] = 'Password3'

sta_if = network.WLAN(network.STA_IF)

def connect_wifi():
   if not sta_if.isconnected():
       sta_if.active(True)
       networks = sta_if.scan()
       for net in networks:
           ssid = net[0].decode()
           if ssid in aps:  
               sta_if.connect(ssid, aps[ssid])
               while not sta_if.isconnected():
                   pass
               break

connect_wifi()
gc.collect()