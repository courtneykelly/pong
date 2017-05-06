from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from ClientSpace import ClientSpace

import cPickle as pickle
import sys

class ClientConnection(Protocol):
	def __init__(self):
		self.cs = ClientSpace()
		self.loop_call = LoopingCall(self.dump)

	def connectionMade(self):
		print "Connected to host"
		self.loop_call.start(1/60)

	def dataReceived(self, data):
		try:
			objects = pickle.loads(data)
			self.cs.update_screen(objects)
		except:
			pass

	def dump(self):
		objects = {}
		objects['player2'] = self.cs.player2.rect.center
		objects['stop'] = self.cs.stop
		package = pickle.dumps(objects)
		self.transport.write(package)

	def connectionLost(self, reason):
		sys.exit("Connection to host lost: {0}".format(reason))

class ClientConnectionFactory(ClientFactory):

	def __init__(self):
		self.clientconn = ClientConnection()

	def buildProtocol(self, addr):
		return self.clientconn

#start listening
reactor.connectTCP('10.12.190.109', 9007, ClientConnectionFactory())
reactor.run()