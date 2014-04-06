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

import cPickle
import hashlib
import sys
import xmlrpclib
import zlib

CODE_ERROR		=	500
CODE_DISABLED		=	405
CODE_NOT_FOUND		=	404
CODE_ALREADY_EXISTS	=	420
CODE_ALREADY_CONNECTED	=	416
CODE_FORBIDDEN		=	403
CODE_FAILED 		=	400
CODE_OK			=	200

class XTCConnector:

	def XTCAuthenticateClient(self, server, login, password, port=8080):
		try:
			
			if server and login:
				self.login = login			
				self.xtcUrl = "https://" + server + ":" + str(port)
				self.xtc = xmlrpclib.ServerProxy(self.xtcUrl)
				self.hashpass = hashlib.sha1( password ).hexdigest()	
				data = { 'channel-id':  'None', 'login': login, 'password': self.hashpass, 'fromCli': 1 }
				response = self.xtc.authenticateClient(data)
				methode, responseCode, userData = response
				authenticationCode, rights, userId = userData

				if responseCode == CODE_OK:
					if authenticationCode == CODE_ERROR:
						raise Exception( "%i Authentication Error" % CODE_ERROR )
					elif authenticationCode == CODE_DISABLED:
						raise Exception( "%i User disabled" % CODE_DISABLED )
					elif authenticationCode == CODE_NOT_FOUND:
						raise Exception( "%i User not found" % CODE_NOT_FOUND )
					elif authenticationCode == CODE_ALREADY_CONNECTED:
						raise Exception( "%i Alreay Connected" % CODE_ALREADY_CONNECTED )
					elif authenticationCode == CODE_FORBIDDEN:
						raise Exception( "%i Bad Password" % CODE_FORBIDDEN )
					elif authenticationCode == CODE_OK:
						print rights
						print userId
					else:
						raise Exception( "Unknwon authentication error" )

				else:
					raise Exception( "Connection Error" )
			else:
				raise Exception("Parameters server and login are mandatory")
	

		except Exception, e:
			print e


	def scheduleTest(self):
		__data = { 'user': self.login, 'user-id': 1, 'prj-id': 1, 'test-id': None, 'background': True,
		  	   'runAt': "(0,0,0,0,0,0)", 'runType': -1, 'runNb': -1, 'withoutProbes': False,
	  		   'debugActivated': False, 'withoutNotif': True, 'noKeepTr': False
		  	   }

		__data.update( { 'testunit': True, 'src': None, 'src2': '', 'properties': None, 'testname': "01_Initial_test", 'testpath': None } )
		pickled = cPickle.dumps(__data)
		commpressed = zlib.compress(pickled)
		dat = xmlrpclib.Binary( commpressed )
		print self.xtc.scheduleTest(self.login, self.hashpass ,dat)
		#wdocument, testId, background = False, runAt = (0,0,0,0,0,0), runType=0, runNb=-1, withoutProbes=False, debugActivated=False, withoutNotif=False, noKeepTr=False, prjId=0
		# runType -1, runAt(0, 0, 0, 0, 0, 0), runNb-1, testName 01_Initial_test, testUser admin, testBack True, runEnabled True, withoutProbe False, debug False, withoutno False, nokeep False, testUserId 1, projectId 1
