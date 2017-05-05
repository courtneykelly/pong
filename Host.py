from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from GameSpace import GameSpace

import cPickle as pickle

class HostConnection(Protocol):
	def __init__(self):
		self.gs = GameSpace()
		self.loop_call = LoopingCall(self.dump)

	def connectionMade(self):
		print "Connected to client"
		start.loop_call.start(.1)

	def dataReceived(self, data):
		pass

	def dump(self):
		self.gs.main_loop()

		# Send ball, paddle positions, scores
		objects = {}
		objects['ball'] = self.gs.ball.rect.center
		objects['player1'] = self.gs.player1.rect.center
		objects['player2'] = self.gs.player2.rect.center
		objects['score1'] = self.gs.score1.rect.center
		objects['score2'] = self.gs.score2.rect.center

		package = pickle.dump(objects)
		self.transport.write(package)

class HostConnectionFactory(Factory):

	def __init__(self):
		self.hostconn = HostConnection()

	def buildProtocol(self, addr):
		return self.hostconn

#start listening
reactor.listenTCP(9007, HostConnectionFactory())
reactor.run()