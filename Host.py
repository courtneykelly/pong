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
		self.loop_call.start(1/60)

	def dataReceived(self, data):
		try:
			objects = pickle.loads(data)
			self.gs.player2.rect.center = objects['player2']
		except:
			pass

	def dump(self):
		self.gs.main_loop()

		# Send ball, paddle positions, scores
		objects = {}
		objects['level'] = self.gs.level
		objects['counter'] = self.gs.counter
		objects['ball1'] = self.gs.ball1.rect.center
		objects['ball2'] = self.gs.ball2.rect.center
		objects['ball3'] = self.gs.ball3.rect.center
		objects['player1'] = self.gs.player1.rect.center
		objects['score1'] = self.gs.score1.score
		objects['score2'] = self.gs.score2.score
		objects['win'] = self.gs.win

		package = pickle.dumps(objects)
		self.transport.write(package)

class HostConnectionFactory(Factory):

	def __init__(self):
		self.hostconn = HostConnection()

	def buildProtocol(self, addr):
		return self.hostconn

#start listening
try: 
	reactor.listenTCP(9007, HostConnectionFactory()) 
	reactor.run()
	print "in try "
except Exception as e:
	print e
finally:
	reactor.stop()