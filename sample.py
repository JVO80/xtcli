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
	ret = myxtcli.scheduleTest("/Samples/Tests_Unit/01_Initial_test","tux")
	print ret

if __name__ == "__main__":
	sys.exit(main())
