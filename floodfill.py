"""###################################################
	FLOOD FILL ALGORITHM BY NIDHI UDACITY
####################################################"""
from maze import Maze
import random
import turtle
import sys

import numpy as np

class floodFill(object):
	def __init__(self, location, heading, goal_bounds, mazeDim):
		print "############################BEGIN FLood fill #############################"

		global mazeWalls, PosR, PosC, direction #This is needed to change the value of these variables
		global GoalR , GoalC ,mazeDepth ,mazeDimension 
		#Assuming maze is 16x16... Robot starts in south west corner.
		#Cell 0,0 (Rows, Columns) is in the Northwest corner.
		 
		# 0...15
		# :
		# 15
		 
		mazeDimension = mazeDim
		#Initial position and direction
		PosR = location[0] #Row position
		PosC = location[1] #Column position
		direction = heading #robots rotation (heading) N, E, S, W
		
		#The goal "cell" (I just used one of the four goal cells).
		GoalR = goal_bounds[0]
		GoalC = goal_bounds[0]
		 
		#Initializing the mazeWalls 3-D Array 16x16x4 (booleans essentially)
		mazeWalls = [0]*mazeDim #maze wall storage NESW
		for j in range(0,mazeDim): #one way of creating nested list
			mazeWalls[j] = [0]*mazeDim
			for k in range(0,mazeDim): 
				mazeWalls[j][k] = [0]*4
		 
		#Initializing the depth array 16x16 signed int
		mazeDepth = [0]*mazeDim #another way of creating nested list (more efficient)
		for i, item in enumerate(mazeDepth): 
			mazeDepth[i] = [0]*mazeDim
			 
	def headingToDirection(self,heading):
		dir_heading = {'u': 'N', 'up': 'N','r': 'E','right': 'E', 'd': 'S','down': 'S' , 'l': 'W' , 'left':'W' } 
		return dir_heading[heading]
	

	def updateWalls(self ,sensing,oldLocation , oldHeading ):

		# global dictionaries for robot movement and sensing
		dir_sensors = {'u': ['l', 'u', 'r'], 'r': ['u', 'r', 'd'],
					   'd': ['r', 'd', 'l'], 'l': ['d', 'l', 'u'],
					   'up': ['l', 'u', 'r'], 'right': ['u', 'r', 'd'],
					   'down': ['r', 'd', 'l'], 'left': ['d', 'l', 'u']}
		dir_move = {'u': [0, 1], 'r': [1, 0], 'd': [0, -1], 'l': [-1, 0],
					'up': [0, 1], 'right': [1, 0], 'down': [0, -1], 'left': [-1, 0]}
		dir_reverse = {'u': 'd', 'r': 'l', 'd': 'u', 'l': 'r',
					   'up': 'd', 'right': 'l', 'down': 'u', 'left': 'r'}
		
		print(sensing,oldLocation , oldHeading )
		curr_cell=[None, None]	   
		leftsensing=sensing[0]
		curr_cell[0]=oldLocation[0]
		curr_cell[1]=oldLocation[1]
		curr_left_direction=dir_sensors[oldHeading][0]
		curr_opp_left_direction=self.headingToDirection(dir_reverse[curr_left_direction])
		while leftsensing>-1:
			leftsensing =leftsensing- 1
			self.cellSetWall(curr_cell[0],curr_cell[1],curr_opp_left_direction)
			curr_cell[0] += dir_move[curr_left_direction][0]
			curr_cell[1] += dir_move[curr_left_direction][1]
			


		straightsensing=sensing[1]
		curr_cell[0]=oldLocation[0]
		curr_cell[1]=oldLocation[1]
		curr_straight_direction=dir_sensors[oldHeading][1]
		curr_opp_straight_direction=self.headingToDirection(dir_reverse[curr_straight_direction])
		while straightsensing>-1:
			straightsensing =straightsensing- 1
			self.cellSetWall(curr_cell[0],curr_cell[1],curr_opp_straight_direction)
			curr_cell[0] += dir_move[curr_straight_direction][0]
			curr_cell[1] += dir_move[curr_straight_direction][1]
			


		rightsensing=sensing[2]
		curr_cell[0]=oldLocation[0]
		curr_cell[1]=oldLocation[1]
		curr_right_direction=dir_sensors[oldHeading][2]
		curr_opp_right_direction=self.headingToDirection(dir_reverse[curr_right_direction])
		while rightsensing>-1:
			self.cellSetWall(curr_cell[0],curr_cell[1],curr_opp_right_direction)
			rightsensing =rightsensing- 1
			curr_cell[0] += dir_move[curr_right_direction][0]
			curr_cell[1] += dir_move[curr_right_direction][1]
			
		
	# This function is called by the simulator to get the
	# next step the mouse should take.
	def nextStep(self ,sensing ,location,heading, oldLocation , oldHeading ):
		print(sensing)
		
		print "#####NEXT STEP"
		PosR = location[0] #Row position
		PosC = location[1] #Column position
		
		self.updateWalls(sensing,oldLocation , oldHeading)
		direction = self.headingToDirection(heading) #robots  (heading) to N, E, S, W
		self.recordWalls()
		self.doFlood()
		nextCell = self.findPath()
	 
		#Debug prints
		print "nextCell: "+str(nextCell)
		print "Direction: "+str(direction)
		print "mazeWalls[PosR][PosC]: "+str(mazeWalls[PosR][PosC])
	 
		 
		if(nextCell == [-1,-1]):
			print "Cannot find path"
			return "Left"
		elif nextCell[0] < PosR: #if next cell is north of robot. 
			#based on the direction of the robot we need to move forward or turn.
			if(direction == "N"): 
				PosR = nextCell[0]
				return "up"
			if(direction == "E"): 
				direction = "N"
				return "left"
			if(direction == "S"): 
				direction = "E"
				return "left"
			if(direction == "W"):
				direction = "N"
				return "right"
		elif nextCell[1] > PosC: #if next cell is east of robot. 
			#based on the direction of the robot we need to move forward or turn.
			if(direction == "N"):
				direction = "E"
				return "right"
			if(direction == "E"): 
				PosC = nextCell[1]
				return "up"
			if(direction == "S"): 
				direction = "E"
				return "left"
			if(direction == "W"):
				direction = "N"
				return "right"
		elif nextCell[0] > PosR: #if next cell is south of robot. 
			#based on the direction of the robot we need to move forward or turn.
			if(direction == "N"): 
				direction = "W"
				return "left"
			if(direction == "E"): 
				direction = "S"
				return "right"
			if(direction == "S"): 
				PosR = nextCell[0]
				return "up"
			if(direction == "W"):
				direction = "S"
				return "left"
		elif nextCell[1] < PosC: #if next cell is west of robot. 
			#based on the direction of the robot we need to move forward or turn.
			if(direction == "N"):
				direction = "W"
				return "left"
			if(direction == "E"): 
				direction = "N"
				return "left"
			if(direction == "S"): 
				direction = "W"
				return "right"
			if(direction == "W"):
				PosC = nextCell[1]
				return "up"
		print "Fail."
		return "right"
	 
		 
		 
	def doFlood(self): #SCAN AND LABEL mazeDepth with distance (depth) values
		global mazeDepth
		 
		#"zero" out depth (Negative one is an unscanned cell)
		for i, index in enumerate(mazeDepth):
			for j, item in enumerate(mazeDepth[i]):
				mazeDepth[i][j] = -1
	 
		  
		mazeDepth[PosR][PosC] = scanDepth = 0 #initialize scan depth and set robot position cell to zero.
		#Iterate (scan) through maze once for each depth to flood. (Robot is at depth 0)
		while(scanDepth < mazeDimension * mazeDimension -1): #(255 is the overflow)
			scanDepth += 1
			for r in range(0,mazeDimension):
				for c in range(0,mazeDimension):
					if mazeDepth[r][c] == -1: #if cell hasn't been labeled (-1)
						if ((r != 0 and mazeWalls[r][c][0] == 0 and mazeDepth[r-1][c] != -1 and mazeDepth[r-1][c] != scanDepth) #Monster IF looks at adjacent cells to the one being scanned
						or (r != mazeDimension-1 and mazeWalls[r][c][2] == 0 and mazeDepth[r+1][c] != -1 and mazeDepth[r+1][c] != scanDepth)#If an adjactent cell isn't separated by a wall and has been 
						or (c != 0 and mazeWalls[r][c][3] == 0 and mazeDepth[r][c-1] != -1 and mazeDepth[r][c-1] != scanDepth) # given a depth then the currently scanned cell is given
						or (c != mazeDimension-1 and mazeWalls[r][c][1] == 0 and mazeDepth[r][c+1] != -1 and mazeDepth[r][c+1] != scanDepth)): # the current depth
							mazeDepth[r][c] = scanDepth
			if mazeDepth[GoalR][GoalC] != -1: #if you have flooded enough to reach the goal position. STOP FLOODING!
				break  
		#PRINT THE MAZE AFTER FLOOD                 
		for i, index in enumerate(mazeDepth):
			print mazeDepth[i]
	 
		 
	 
	def findPath(self ): 
		#Starting at the goal, find the shortest path back to the robot.
		r = GoalR #These r and c are the coordinates of the cell being observed. (starting at the goal cell)
		c = GoalC
		scanDepth = mazeDepth[r][c] #this is the depth to the observed cell.
		while(scanDepth > 0):
			#If a cell with one less depth is next to the observed cell (with no walls separating) Then OBSERVE THAT CELL NEXT!
			#If that cell you want to observe next has the robot in it, 
			if (r != mazeDimension and mazeWalls[r][c][2] == 0 and mazeDepth[r+1][c] == scanDepth-1):  #LOOK SOUTH (from observed cell)
				if(scanDepth-1 == 0): return [r,c] #Return the next cell the robot should travel to. (if that cell is depth 0 (robot))
				r += 1
			elif (r != 0 and mazeWalls[r][c][0] != 1 and mazeDepth[r-1][c] == scanDepth-1): #LOOK NORTH 
				if(scanDepth-1 == 0): return [r,c] 
				r -= 1
			elif (c != mazeDimension and mazeWalls[r][c][1] != 1 and mazeDepth[r][c+1] == scanDepth-1): #LOOK EAST
				if(scanDepth-1 == 0): return [r,c]
				c += 1
			elif (c != 0 and mazeWalls[r][c][3] != 1 and mazeDepth[r][c-1] == scanDepth-1): #LOOK WEST
				if(scanDepth-1 == 0): return [r,c]
				c -= 1
			else:
				return [-1,-1]
				 
			scanDepth -=1 #Seet the new depth of the observed cell.
	 
		return [-1,-1]
	 
	 
		 
	 
	def recordWalls(self): #This is run each step. It records the current walls in the memory matrix (mazeWalls).
		if(direction == "N"):
			if maze.isWallFront():
				wallSetN(PosR,PosC)
			if maze.isWallRight():
				wallSetE(PosR,PosC)
			if maze.isWallBack():
				wallSetS(PosR,PosC)
			if maze.isWallLeft():
				wallSetW(PosR,PosC)
		elif(direction == "E"):
			if maze.isWallFront():
				wallSetE(PosR,PosC)
			if maze.isWallRight():
				wallSetS(PosR,PosC)
			if maze.isWallBack():
				wallSetW(PosR,PosC)
			if maze.isWallLeft():
				wallSetN(PosR,PosC)
		elif(direction == "S"):
			if maze.isWallFront():
				wallSetS(PosR,PosC)
			if maze.isWallRight():
				wallSetW(PosR,PosC)
			if maze.isWallBack():
				wallSetN(PosR,PosC)
			if maze.isWallLeft():
				wallSetE(PosR,PosC) 
		elif(direction == "W"):
			if maze.isWallFront():
				wallSetW(PosR,PosC)
			if maze.isWallRight():
				wallSetN(PosR,PosC)
			if maze.isWallBack():
				wallSetE(PosR,PosC)
			if maze.isWallLeft():
				wallSetS(PosR,PosC)     
	 
	#set wall at given direction in a cell
	def cellSetWall(self, row, col, heading):
		print(row, col, heading)
		if(heading == "N"):
			self.wallSetN(row,col)
		elif(heading == "E"):
			self.wallSetE(row,col)
		elif(heading == "S"):
			self.wallSetS(row,col)
		elif(heading == "W"):
			 self.wallSetW(row,col)    

	def wallSetN(self,Row,Col):
		global mazeWalls
		mazeWalls[Row][Col][0] = 1
		if Row > 0: # if there is then set the "same" wall in the cell right above (south wall)
			mazeWalls[Row - 1][Col][2] = 1
		 
	def wallSetE(self,Row,Col):
		global mazeWalls
		mazeWalls[Row][Col][1] = 1
		if (Col < len(mazeWalls[Row])-1):
			mazeWalls[Row][Col + 1][3] = 1
			 
	def wallSetS(self,Row,Col):
		global mazeWalls
		mazeWalls[Row][Col][2] = 1
		if (Row < len(mazeWalls)-1): # if there is then set the "same" wall in the cell right above (south wall)
			mazeWalls[Row + 1][Col][0] = 1
	 
	def wallSetW(self,Row,Col):
		global mazeWalls
		mazeWalls[Row][Col][3] = 1
		if (Col > 0):
			mazeWalls[Row][Col - 1][1] = 1
