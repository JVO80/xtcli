#!/usr/bin/env python
#-*- coding: utf-8 -*-

# -------------------------------------------------------------------
# Copyright (c) 2014 eXtensive Testing Organization
#
# author : Jean-Vianney OBLIN
# mail :
# description : install script for xtcli
#
# This file is part of the XTC Project
# -------------------------------------------------------------------

import sys
from distutils.core import setup

NAME = "xtcpyrc"
DESCRIPTION = "XTC PYthon Remote Controller : Allows to start tests from a python software"
AUTHOR = "Jean-Vianney OBLIN"
EMAIL = "contact@extensivetesting.org"
URL = "http://www.extensivetesting.org"

def main():

	setup(name = NAME,
	      version='1.0',
      	      description = DESCRIPTION,
              author = AUTHOR,
              author_email = EMAIL ,
              packages = ['xtcpyrc'],
              scripts = ["setup.py"],
              url = URL,
              license = ["LGPL"],
      ) 	

if __name__ == "__main__":
	sys.exit(main())
	
