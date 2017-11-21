# MicroMouseAi

to change algorithm change do changes in robot.py

#self.algoObj=  AlgoPackage('random' ,self.location, self.heading,self.goal_bounds, self.maze_dim )
self.algoObj=  AlgoPackage('floodfill' ,self.location, self.heading,self.goal_bounds, self.maze_dim )
#self.algoObj=  AlgoPackage('dfs' ,self.location, self.heading,self.goal_bounds, self.maze_dim )
#self.algoObj=  AlgoPackage('bfs' ,self.location, self.heading,self.goal_bounds, self.maze_dim )
