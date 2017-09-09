import numpy as np
from maze import Maze
import random
import turtle
import sys

class AlgoPackage(object):
	def __init__(self, typeOfAlgo , mazeDim):

		"""
		taking type of algo
		"""
		self.algoType = typeOfAlgo
		self.mazeDim = mazeDim
		#self.graphAdjacencyMatrix=self.buildAdjacencyGraph(self.mazeObj)

		if self.algoType == "Djskitra":
			self.callDjkistra(self.mazeObj)

		elif self.algoType == "random":
			self.callRandom()
		else:
			print("No specific  algorithm  mentioned")



	def callRandom(self):
		print "calling random algo"
		possible_movement = [-3, -2, -1, 0, 1 , 2,3]
		possible_rotation=[-90 ,0 ,90]
		return (random.choice(possible_rotation) ,random.choice(possible_movement))


	def buildAdjacencyGraph(self):
		pass


	def callDjkistra(self ,graphs_Adjacency_list):
		print "calling djisktra shortest path for non negative weights"







