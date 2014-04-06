from xtcl import *
import unittest

class xtclTestCase(unittest.TestCase):

	def setUp(self):
		self.xtcCnx = XTCConnector()

	def tearDown(self):
		self.xtcCnx = None

	def testServerName(self):
		""" check that an empty server parameter generate an exception """
		self.assertRaises(Exception, self.xtcCnx.XTCAuthenticateClient , "", login="admin", password="")
		#try:
		#	self.xtcCnx.XTCAuthenticateClient("",login="admin",password="")
		#except Exception:
                #	pass
	        #else:
        	#        print("expected an Exception for empty server")

	def testServerLogin(self):
		""" check that an empty login generate an exception """
		try:
                        self.xtcCnx.XTCAuthenticateClient("tas.dmachard.net",login="",password="")
                except Exception:
                        pass
                else:
                        print("expected an Exception for empty login")

if __name__ == "__main__":
	unittest.main()	
