from Naked.toolshed.shell import execute_js
import socket
import struct
import binascii
import time
import json
import urllib2
import os

oldtime = time.time()
print "Now sniffing the network for Dash units..."
# Use your own IFTTT key, not this fake one
ifttt_key = 'PUT IFTTT key here'
# Set these up at https://ifttt.com/maker
ifttt_url_dashbell = 'https://maker.ifttt.com/trigger/dashdoorbell_press/with/key/' + ifttt_key
ifttt_url_ON_button = 'https://maker.ifttt.com/trigger/ON_button/with/key/' + ifttt_key

# Replace these fake MAC addresses and nicknames with your own
macs = {
    '000f6006fa71' : 'chromebook',
    '5c514f29e50f' : 'macbook',
    '7824af908208' : 'nexus6',
    '2c3453455541' : 'apple_tv',
    '7475482d15bb' : 'dash_glad',
    'a002dccb5473' : 'dash_hefty',
    'a002dc342332' : 'dash_ON1',
    '0024d7a6b3e0' : 'something else',
}

# Trigger a IFTTT URL. Body includes JSON with timestamp values.
def trigger_url(url):
    data = '{ "value1" : "' + time.strftime("%Y-%m-%d") + '", "value2" : "' + time.strftime("%H:%M") + '" }'
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    response = f.read()
    f.close()
    return response

def record_dashbell():
    print 'triggering dashbell event, response: ' + trigger_url(ifttt_url_dashbell)

def record_ON_button():
    print 'triggering the griddle, response: ' + trigger_url(ifttt_url_ON_button)

rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

while True:
    packet = rawSocket.recvfrom(2048)
    ethernet_header = packet[0][0:14]
    ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)
    arp_header = packet[0][14:42]
    arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)
    # skip non-ARP packets
    ethertype = ethernet_detailed[2]
    if ethertype != '\x08\x06':
        continue
    source_mac = binascii.hexlify(arp_detailed[5])
    source_ip = socket.inet_ntoa(arp_detailed[6])
    dest_ip = socket.inet_ntoa(arp_detailed[8])
    if source_mac in macs:
       # print "ARP from " + macs[source_mac] + " with IP " + source_ip
        if macs[source_mac] == 'dash_glad':
           if time.time() - oldtime > 15:
              record_dashbell()
              oldtime = time.time()
           else:
              print eval('time.time()-oldtime')
        if macs[source_mac] == 'dash_hefty':
	   if time.time() - oldtime > 40:
              print "SUMMON THE BURRITOBOT"
              execute_js('/home/pi/bin/node_modules/chipsandguac/burrito_order.js')
              oldtime = time.time()
           else:
              print "THE BURRITOBOT HAS FINISHED AND MUST SLUMBER!!"
        if macs[source_mac] == 'dash_ON1':
           if time.time() - oldtime > 1:
              record_ON_button()
              oldtime = time.time()
              print "Griddle ON!"
           else:
              print "Duplicate Ignored..."

    else:
        print "Unknown MAC " + source_mac + " from IP " + source_ip

