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


setup(name='xtcpyrc',
      version='1.0',
      description='XTC PYthon Remote Controller : Allows to start tests from a python software',
      author='Jean-Vianney OBLIN',
      author_email='contact@extensivetesting.org',
      packages = ['xtcpyrc'],
      scripts = ["setup.py"],
      url = 'http://www.extensivetesting.org',
      license = ["LGPL"],
      ) 	
