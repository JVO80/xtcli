#!/usr/bin/env python
#-*- coding: utf-8 -*-

# -------------------------------------------------------------------
# Copyright (c) 2014 eXtensive Testing Organization
#
# author : Jean-Vianney OBLIN
# mail :
#
# This file is part of the XTC Project
# -------------------------------------------------------------------

from xtcpyrc.xtcpyrc import *
import sys

def main():
	myxtcli = SrvConnector(server="tas.dmachard.net",login="jvotestcli",password="",port=8080, path="/")
	ret = myxtcli.scheduleTest("/Samples/Tests_Suite/Tests_Agents/02_ARP","tsx")
	if ret == "SUCCESS":
		print "Test scheduled"
		return 0
	else:
		print "Test not scheduled"
		return 1

if __name__ == "__main__":
	sys.exit(main())
