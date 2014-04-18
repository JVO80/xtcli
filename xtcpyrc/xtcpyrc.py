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

from os.path import basename
import hashlib
import json
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

class SrvConnector:

	def __init__(self, server, login, password, port=80, https=True, path="/xmlrpc/"):
		"""
		Constructor for SrvConnector

		@param server: IP or FQDN
		@type server: string

		@param login: your login
		@type login: string

		@param password: your password
		@type password: string
		
		@param port: tcp port to connect on server. Default is 80.
		@type port: int 
		"""
		try:
			if server and login:
                                self.login = login
				if https:
					proto = "https://"
				else:
					proto = "http://"
	                        self.server_url = proto + server + ":" + str(port) + path
                                self.srv = xmlrpclib.ServerProxy(self.server_url)
                                self.hash_pass = hashlib.sha1( password ).hexdigest()
			else:
				raise ValueError( "Server and Login can't be empty" ) 
                except xmlrpclib.ProtocolError as err:
			print "A protocol error occurred"
			print "URL: %s" % err.url
			print "HTTP/HTTPS headers: %s" % err.headers
			print "Error code: %d" % err.errcode
			print "Error message: %s" % err.errmsg

		
	def scheduleTest(self, path, extension):
		""" 
		Allows to start remotely a test on TAS 
			
		@param path: path of the the test on TAS without extension 
		@type path: string

		@param testname:
		@type testname:

		@param extension: extension of the test (tux, ...)
		@type extension: string

		@rtype : tbd
		@return: tbd
		"""

		try:

			if not path:
				raise ValueError("path parameter can't be empty")
			if not extension:
				raise ValueError("extension parameter can't be empty")
	
			filename = basename(path)
	
			data = { 'nocontent': True ,
        	                 'testextension': extension,
                	         'prj-id': 1,
     	        	         'testpath': path,
        	                 'testname': filename,
         	      	         'user-id': 8,
	                         'user': self.login,
        	                 'test-id': 0,
                	         'background': True,
            	        	 'runAt': (0,0,0,0,0,0),
     			         'runType': 1,
       		                 'runNb': 1,
                	         'withoutProbes': False,
   		                 'debugActivated': False,
                		 'withoutNotif': False,
                  	         'noKeepTr': False
                       		 }

			jsoned = json.dumps(data)
        		commpressed = zlib.compress(jsoned)
			xml_rpc_data = xmlrpclib.Binary(commpressed)
			fromCli = xmlrpclib.Boolean(True)
			response = self.srv.scheduleTest( self.login, self.hash_pass, xml_rpc_data, fromCli ) 
			methode, responseCode, responseData = response
			
			""" For scheduleTest, authenticateClient method is returned if an authentication error occurs"""
			if methode == "authenticateClient":
				authenticationCode, other = responseData
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
                                else:
                                        raise Exception( "Unknwon authentication error" )
			elif methode == "scheduleTest":			
				if responseCode == CODE_OK:
					taskId, testId, testName, background, recursive, postponed, successive = responseData
					ret = "SUCCESS"
				elif responseCode == CODE_ERROR:
					ret = "FAILED"		
			else:
				raise Exception( "Unknown xmlrpc method" )		
		except xmlrpclib.Fault, err:
			errorMsg = "XMLRPCLIB Fault : %d %s" % (err.faultCode, err.faultString)
			ret = errorMsg		
		return ret
