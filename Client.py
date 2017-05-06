from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from ClientSpace import ClientSpace

import cPickle as pickle

class ClientConnection(Protocol):
	def __init__(self):
		self.cs = ClientSpace()
		self.loop_call = LoopingCall(self.dump)

	def connectionMade(self):
		print "Connected to host"
		self.loop_call.start(.25)

	def dataReceived(self, data):
		try:
			objects = pickle.loads(data)
			self.cs.update_screen(objects)
		except:
			pass

	def dump(self):
		objects = {}
		objects['player2'] = self.cs.player2.rect.center
		package = pickle.dumps(objects)
		self.transport.write(package)

class ClientConnectionFactory(ClientFactory):

	def __init__(self):
		self.clientconn = ClientConnection()

	def buildProtocol(self, addr):
		return self.clientconn

#start listening
reactor.connectTCP('10.12.190.109', 9007, ClientConnectionFactory())
reactor.run()