#!/usr/bin/env python
#-*- coding: utf-8 -*-

from xtcpyrc.xtcpyrc import *
import unittest2
import xmlrunner
import xmlrpclib

class xtclTestCase(unittest2.TestCase):

	def setUp(self):
		self.login = "jvotestcli"
                self.password = ""
                self.badlogin = "badlogin"
                self.badpassword = "badpassword"
		self.server = "tas.dmachard.net"
		self.badserver = "tas.toto.titi"
		self.badport = 1719
		self.path = "/Samples/Tests_Unit/01_Initial_test"
		self.invalidPath = "/titi/toto"
		self.ext = "tux"
		self.invalidExt = "titi"
		

	def tearDown(self):
		pass

	""" Nominal """
	def testUnitNominal(self):
		""" Check nominal behaviour """
		srv = SrvConnector(self.server, self.login, self.password, port=8080, path="/")
		self.assertEqual(srv.scheduleTest( self.path, self.ext ), "SUCCESS")

	

	""" Tests for __init__() """

	def testServerName(self):
		""" check that an empty server parameter generate an exception """
		self.assertRaises(ValueError, SrvConnector,"", self.login, self.password, port=8080, path="/")

	def testServerLogin(self):
		""" check that an empty login generate an exception """
		self.assertRaises(ValueError, SrvConnector,self.server, "", self.password, port=8080, path="/")

	#def testBadServer(self):
		""" [Errno -2] Name or service not known : Seems to be an exit """
	#	self.assertRaises(SocketError, SrvConnector,self.badserver, self.login, self.password, port=8080, path="/")

	#def testBadPort(self):
		""" [Errno 110] Connection timed out : Seems to be an exit """
	#	 self.assertRaises(ValueError, SrvConnector,self.server, "", self.password, port=self.badport, path="/")

	#def testHttpInsteadHttps(self):
		""" xmlrpclib.ProtocolError don't work"""
	#	self.assertRaises(xmlrpclib.ProtocolError, SrvConnector,self.server, self.login, self.password, port=8080, https=False, path="/")


	""" Authentication Test """
	
	def testUserNotFound(self):
                """ check that a bad login generates an exception """
                srv = SrvConnector(self.server, self.badlogin, self.password, port=8080, path="/")
		self.assertRaises(Exception, srv.scheduleTest, self.path, self.ext)

	def badPassword(self): 
		""" check that a bad password generates an exception """
                srv = SrvConnector(self.server, self.login, self.badpassword, port=8080, path="/")
                self.assertRaises(Exception, srv.scheduleTest, self.path, self.ext)

	""" Tests for scheduleTest """

	def testNoPath(self):
		""" check that an empty path generates a ValueError """
		srv = SrvConnector(self.server, self.login, self.password, port=8080, path="/")
		self.assertRaises(ValueError, srv.scheduleTest, "", self.ext)

	def testNoTestExtension(self):
		""" check that an empty extension parameter generates a ValueError """
                srv = SrvConnector(self.server, self.login, self.password, port=8080, path="/")
                self.assertRaises(ValueError, srv.scheduleTest, self.path, "")

	def testBadPath(self):
		""" check that an invalid path parameter generates an error """
		srv = SrvConnector(self.server, self.login, self.password, port=8080, path="/")
		self.assertEqual(srv.scheduleTest( self.invalidPath, self.ext ), "FAILED")

	def testBadExt(self):
		""" check that an invalid extension parameter generates an error """
                srv = SrvConnector(self.server, self.login, self.password, port=8080, path="/")
                self.assertEqual(srv.scheduleTest( self.path, self.invalidExt ), "FAILED")	
		
	

if __name__ == "__main__":
	unittest2.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))	
