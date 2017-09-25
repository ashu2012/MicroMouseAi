"""###################################################
	FLOOD FILL ALGORITHM BY NIDHI UDACITY
####################################################"""
from maze import Maze
import random
import turtle
import sys
import pdb
import numpy as np

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def printst(self):
		print(self.items)


class floodFill(object):
	def __init__(self, location, heading, goal_bounds, mazeDim):
		print "############################BEGIN FLood fill #############################"

		global stackNext 
		stackNext = Stack()
		global mazeWalls, PosR, PosC, direction  #This is needed to change the value of these variables
		global GoalR , GoalC ,mazeDepth ,mazeDimension ,scanDepth 
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

		global mazeDepth
		 
		#"zero" out depth (Negative one is an unscanned cell)
		for i, index in enumerate(mazeDepth):
			for j, item in enumerate(mazeDepth[i]):
				mazeDepth[i][j] = -1
	 
		  
		mazeDepth[PosR][PosC] = scanDepth = 0 #initialize scan depth and set robot position cell to zero.
		#Iterate (scan) through maze once for each depth to flood. (Robot is at depth 0)


			 
	def headingToDirection(self,heading):
		dir_heading = {'u': 'N', 'up': 'N','r': 'E','right': 'E', 'd': 'S','down': 'S' , 'l': 'W' , 'left':'W' } 
		return dir_heading[heading]
	

	def headingToRotation(self,direction):
		dir_heading = {'f': 0, 'forward': 0,'r': -90,'right': -90,'l': 90 , 'left':90 } 
		return dir_heading[direction]

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
		curr_opp_left_direction=self.headingToDirection(curr_left_direction)
		while leftsensing>0:
			leftsensing =leftsensing- 1
			self.cellSetWall(curr_cell[0],curr_cell[1],curr_opp_left_direction)
			print "mazeWalls["+str(curr_cell[0])+"]["+str(curr_cell[1])+"]: "+str(mazeWalls[curr_cell[0]][curr_cell[1]])
			curr_cell[0] += dir_move[curr_left_direction][0]
			curr_cell[1] += dir_move[curr_left_direction][1]
			


		straightsensing=sensing[1]
		curr_cell[0]=oldLocation[0]
		curr_cell[1]=oldLocation[1]
		curr_straight_direction=dir_sensors[oldHeading][1]
		curr_opp_straight_direction=self.headingToDirection(curr_straight_direction)
		while straightsensing>0:
			straightsensing =straightsensing- 1
			self.cellSetWall(curr_cell[0],curr_cell[1],curr_opp_straight_direction)
			print "mazeWalls["+str(curr_cell[0])+"]["+str(curr_cell[1])+"]: "+str(mazeWalls[curr_cell[0]][curr_cell[1]])
			curr_cell[0] += dir_move[curr_straight_direction][0]
			curr_cell[1] += dir_move[curr_straight_direction][1]
			

		rightsensing=sensing[2]
		curr_cell[0]=oldLocation[0]
		curr_cell[1]=oldLocation[1]
		curr_right_direction=dir_sensors[oldHeading][2]
		curr_opp_right_direction=self.headingToDirection(curr_right_direction)
		while rightsensing>0:
			self.cellSetWall(curr_cell[0],curr_cell[1],curr_opp_right_direction)
			print "mazeWalls["+str(curr_cell[0])+"]["+str(curr_cell[1])+"]: "+str(mazeWalls[curr_cell[0]][curr_cell[1]])
			rightsensing =rightsensing- 1
			curr_cell[0] += dir_move[curr_right_direction][0]
			curr_cell[1] += dir_move[curr_right_direction][1]
		
	def printMaze(self):
		#PRINT THE MAZE AFTER FLOOD 
		pdb.set_trace()                
		for j in range(len(mazeDepth)-1, -1,-1):
			for i in range(0,len(mazeDepth), 1):
				print mazeDepth[i][j] ,
			print
	# This function is called by the simulator to get the
	# next step the mouse should take.
	def nextStep(self ,sensing ,location,heading, oldLocation , oldHeading ):
		print(sensing)
		
		print "#####NEXT STEP"
		PosR = location[1] #Row position
		PosC = location[0] #Column position
		
		self.updateWalls(sensing,location , heading)
		direction = self.headingToDirection(heading) #robots  (heading) to N, E, S, W
		#self.recordWalls()
		
		
		nextCell = self.doFlood().next()
		
		self.printMaze()
		#Debug prints
		print "nextCell: "+str(nextCell)
		print "Current Direction: "+str(direction)
		print "mazeWalls["+str(PosC)+"]["+str(PosR)+"]: "+str(mazeWalls[PosC][PosR])
	 	
	 	# once exploreation  done find path
		#nextCell = self.findPath(nextCell)

	 	stackNext.printst()
		 
		if(nextCell == [-1,-1]):
			print "Cannot find path"
			return "Left"
		elif nextCell[1] < PosR: #if next cell is South of robot. 
			#based on the direction of the robot we need to move forward or turn.
			if(direction == "S"): 
				PosR = nextCell[0]
				return (self.headingToRotation("forward") ,1)
			if(direction == "E"): 
				direction = "S"
				return (self.headingToRotation("right") ,0)
			if(direction == "N"): 
				direction = "E"
				return (self.headingToRotation("right") ,0)
			if(direction == "W"):
				direction = "S"
				return (self.headingToRotation("left") ,0)
		elif nextCell[0] > PosC: #if next cell is east of robot. 
			#based on the direction of the robot we need to move forward or turn.
			if(direction == "N"):
				direction = "E"
				return (self.headingToRotation("right") ,0)
			if(direction == "E"): 
				PosC = nextCell[1]
				return (self.headingToRotation("forward") ,1)
			if(direction == "S"): 
				direction = "E"
				return (self.headingToRotation("left") ,0)
			if(direction == "W"):
				direction = "N"
				return (self.headingToRotation("right") ,0)
		elif nextCell[1] > PosR: #if next cell is North of robot. 
			#based on the direction of the robot we need to move forward or turn.
			if(direction == "N"): 
				direction = "N"
				PosR = nextCell[0]
				return (self.headingToRotation("forward") ,1)
			if(direction == "E"): 
				direction = "N"
				return (self.headingToRotation("left") ,0)
			if(direction == "S"): 
				direction = "E"
				return (self.headingToRotation("left") ,0)
			if(direction == "W"):
				direction = "N"
				return (self.headingToRotation("right") ,0)
		elif nextCell[0] < PosC: #if next cell is west of robot. 
			#based on the direction of the robot we need to move forward or turn.
			if(direction == "N"):
				direction = "W"
				return (self.headingToRotation("left") ,0)
			if(direction == "E"): 
				direction = "N"
				return (self.headingToRotation("left") ,0)
			if(direction == "S"): 
				direction = "W"
				return (self.headingToRotation("right") ,0)
			if(direction == "W"):
				PosC = nextCell[1]
				return (self.headingToRotation("forward") ,1)
		else:
			print "Fail."
			return (self.headingToRotation("right") ,0)
	 
		 
	def doFlood(self): #SCAN AND LABEL mazeDepth with distance (depth) values
		scanDepth =mazeDepth[0][0]
		nextCell=[]
		while(scanDepth < mazeDimension * mazeDimension -1): #(255 is the overflow)
			scanDepth += 1
			for x in range(0,mazeDimension):
				for y in range(0,mazeDimension):
					if mazeDepth[x][y] == -1 : #if cell hasn't been labeled (-1)
						if ((x != 0 and mazeWalls[x][y][3] == 1 and mazeDepth[x-1][y] != -1 and mazeDepth[x-1][y] != scanDepth) #Monster IF looks at adjacent cells to the one being scanned
						or (x != mazeDimension-1 and mazeWalls[x][y][1] == 1 and mazeDepth[x+1][y] != -1 and mazeDepth[x+1][y] != scanDepth)#If an adjactent cell isn't separated by a wall and has been 
						or (y != 0 and mazeWalls[x][y][2] == 1 and mazeDepth[x][y-1] != -1 and mazeDepth[x][y-1] != scanDepth) # given a depth then the currently scanned cell is given
						or (y != mazeDimension-1 and mazeWalls[x][y][0] == 1 and mazeDepth[x][y+1] != -1 and mazeDepth[x][y+1] != scanDepth)): # the current depth
							print(x,y)
							print(mazeWalls[x][y])
							mazeDepth[x][y] = scanDepth
							nextCell=[x,y]
							stackNext.push([x,y,scanDepth])
							yield nextCell
			if mazeDepth[GoalR][GoalC] != -1: #if you have flooded enough to reach the goal position. STOP FLOODING!
				nextCell=[GoalC,GoalR]
				yield nextCell
			  
		
	 
		yield nextCell
	 
	def findPath(self, nextCell): 
		#Starting at the goal, find the shortest path back to the robot.
		r = nextCell[0] #These r and c are the coordinates of the cell being observed. (starting at the goal cell)
		c = nextCell[1]
		scanDepth = mazeDepth[r][c] #this is the depth to the observed cell.
		while(scanDepth > 0):
			#If a cell with one less depth is next to the observed cell (with no walls separating) Then OBSERVE THAT CELL NEXT!
			#If that cell you want to observe next has the robot in it, 
			if (r != mazeDimension and mazeWalls[r][c][2] == 1 and mazeDepth[r+1][c] == scanDepth-1):  #LOOK SOUTH (from observed cell)
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
	 
	 
		 
	 
	#set wall at given direction in a cell
	def cellSetWall(self, x, y, heading):
		print( x,y, heading)
		if(heading == "N"):
			self.wallSetN(x,y)
		elif(heading == "E"):
			self.wallSetE(x,y)
		elif(heading == "S"):
			self.wallSetS(x,y)
		elif(heading == "W"):
			 self.wallSetW(x,y)    

	def wallSetS(self,x,y):
		global mazeWalls
		mazeWalls[x][y][2] = 1
		if y > 0: # if there is then set the "same" wall in the cell right below (south wall)
			mazeWalls[x][y][0] = 1
		 
	def wallSetE(self,x,y):
		global mazeWalls
		mazeWalls[x][y][1] = 1
		if (x < len(mazeWalls[x])-1):
			mazeWalls[x+1][y][3] = 1
			 
	def wallSetN(self,x,y):
		global mazeWalls
		mazeWalls[x][y][0] = 1
		if (y < len(mazeWalls)-1): # if there is then set the "same" wall in the cell right above (south wall)
			mazeWalls[x][y+1][2] = 1
	 
	def wallSetW(self,x,y):
		global mazeWalls
		mazeWalls[x][y][3] = 1
		if (x > 0):
			mazeWalls[x-1][y][1] = 1
