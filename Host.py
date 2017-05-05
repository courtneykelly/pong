from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from GameSpace import GameSpace

class HostConnection(Protocol):
	def __init__(self):
		self.gs = GameSpace()
		self.loop_call = LoopingCall(self.dump)

	def connectionMade(self):
		print "Connected to client"

	def dataReceived(self, data):
		pass

	def dump(self):
		pass

class HostConnectionFactory(Factory):

	def __init__(self):
		self.hostconn = HostConnection()

	def buildProtocol(self, addr):
		return self.hostconn

#start listening
reactor.listenTCP(9007, HostConnectionFactory())
reactor.run()