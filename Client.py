from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from ClientSpace import ClientSpace
from Address import HOST_ADDRESS
from Address import PORT

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
		if self.cs.stop == 1:
			self.transport.loseConnection()
		package = pickle.dumps(objects)
		self.transport.write(package)

	def connectionLost(self, reason):
		reactor.stop()

class ClientConnectionFactory(ClientFactory):

	def __init__(self):
		self.clientconn = ClientConnection()

	def buildProtocol(self, addr):
		return self.clientconn

# Connect to Host
reactor.connectTCP(HOST_ADDRESS, PORT, ClientConnectionFactory())
reactor.run()
print "Exited successfully, thanks for playing!"
sys.exit(0)