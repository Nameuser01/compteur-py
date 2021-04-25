#!/usr/bin/env python3
#coding utf-8

import threading
import time
def test():
	#programme de test de la classe Counter
	x = Counter("a", True, 20, 10, 1)
	y = Counter("b", False, 10, 15, 2)
	x.start()
	y.start()

class Counter(threading.Thread):

	def __init__(self, nom, desc, initNbr, endNbr, timeToSleep):
		threading.Thread.__init__(self)
		assert isinstance (nom, str) and (len(nom) > 0)
		assert isinstance (desc, bool)
		assert isinstance (initNbr, float) or (initNbr, int)
		assert isinstance (endNbr, float) or (endNbr, int)
		assert isinstance (timeToSleep, int)
		self.desc = desc
		self.initNbr = initNbr
		self.endNbr = endNbr
		self.timeToSleep = timeToSleep
		self.nom = nom

	def run(self):
		if self.desc == True:
			#Boucle qui décrémente la valeur de départ pour arriver à la valeur d'arrivée
			while(self.initNbr > self.endNbr):
				self.initNbr -= 1
				time.sleep(self.timeToSleep)
				print("{} vaut {}".format(self.nom, self.initNbr))
		else:
			#Boucle qui incrémente la valeur de départ pour arriver à la valeur d'arrivée
			while(self.initNbr < self.endNbr):
				self.initNbr += 1
				time.sleep(self.timeToSleep)
				print("{} vaut {}".format(self.nom, self.initNbr))


test()