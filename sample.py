#!/usr/bin/env python
from xtcli import *

try:
	myxtcli = XTCConnector()
	myxtcli.XTCAuthenticateClient("tas.dmachard.net","admin","")
except Exception, e:
	print e
#myxtc.scheduleTest()

