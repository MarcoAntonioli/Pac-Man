import pygame
from random import randint 

mul = 2
width = 8 * 28 * mul
height = 8 * 31 * mul
dimension = 8 * mul
background = (0,0,0)
#white = (255,255,255)
blue = (20,20,200)
yellow = (255,255,0)
red = (255, 0, 0)
brilliant_levender = (255, 184, 255)
acqua = (0, 255, 255)
pastel_orange = (255, 184, 82)

map_ = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],		#1
[0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0],		#2			
[0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],		#3			
[0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],		#4			
[0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],		#5			
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],		#6				
[0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0],		#7			
[0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0],		#8				
[0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0],		#9			
[0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],		#10			
[0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],		#11			
[0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0],		#12		
[0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0],		#13		
[0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0],		#14		
[0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0],		#15		
[0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0],		#16		
[0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],		#17		
[0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0],		#18		
[0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],		#19		
[0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],		#20		
[0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0],		#21		
[0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],		#22		
[0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],		#23		
[0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0],		#24		
[0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0],		#25		
[0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0],		#26		
[0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0],		#27		
[0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0],		#28		
[0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0],		#29	
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],		#30
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],		#31	
]

def grid(screen,widht,height):
	screen.fill(background)
	for i in range(len(map_)):
		for j in range(len(map_[i])):
			if not map_[i][j]:
				pygame.draw.rect(screen,blue,[j*dimension+1,i*dimension+1,dimension-1,dimension-1])

def pacman(surface,x,y):
	pygame.draw.rect(surface,yellow,[x,y,dimension+1,dimension+1])

def ghosts(surface):
	pygame.draw.rect(surface,red,[12*dimension,14*dimension,dimension+1,dimension+1])
	pygame.draw.rect(surface,brilliant_levender,[13*dimension,14*dimension,dimension+1,dimension+1])
	pygame.draw.rect(surface,acqua,[14*dimension,14*dimension,dimension+1,dimension+1])
	pygame.draw.rect(surface,pastel_orange,[15*dimension,14*dimension,dimension+1,dimension+1])

def movement(event,x_update,y_update,direction):							
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_update = -dimension//2
			y_update = 0
			direction = 'left'
		elif event.key == pygame.K_RIGHT:
			x_update = dimension//2
			y_update = 0
			direction = 'right'
		elif event.key == pygame.K_UP:
			x_update = 0
			y_update = -dimension//2
			direction = 'up'
		elif event.key == pygame.K_DOWN:
			x_update = 0
			y_update = dimension//2
			direction = 'down'
	return x_update, y_update, direction	


def tunnel(x,y,screen):
	if x == 26 * dimension and y == 14 * dimension:
		x = dimension 
		pygame.draw.rect(screen,yellow,[26*dimension,14*dimension,dimension+1,dimension+1])
	elif x == dimension and y == 14 * dimension:
		x = 26 * dimension
		pygame.draw.rect(screen,yellow,[dimension,14*dimension,dimension+1,dimension+1])
	return x, y

def stop(x,y,x_update,y_update,direction):
	for i in range(len(map_)):
		for j in range(len(map_[i])):
			if not (i == 14 * dimension and j == dimension) or (i == 14 * dimension and j == 26 * dimension):
				if map_[i][j] == 0 and direction == 'up':
					# if x == j * dimension and y == (i+1) * dimension:
					# 	y_update = 0
					if ((0 <= x - j * dimension < dimension) or (0 < (x + dimension) - j * dimension < dimension)) and (y == (i+1) * dimension):
						y_update = 0
				elif map_[i][j] == 0 and direction == 'left':
					# if x == (j+1) * dimension and y == i * dimension:
					# 	x_update = 0
					if x == (j+1) * dimension and ((0 <= y - i * dimension < dimension) or (0 < (y + dimension) - i * dimension < dimension)):
						x_update = 0
				elif map_[i][j] == 0 and direction == 'down':
					# if x == j * dimension and y == (i-1) * dimension:
					# 	y_update = 0
					if ((0 <= x - j * dimension < dimension) or (0 < (x + dimension) - j * dimension < dimension)) and (y == (i-1) * dimension):
						y_update = 0
				elif map_[i][j] == 0 and direction == 'right':
					# if x == (j-1) * dimension and y == i * dimension:
					# 	x_update = 0
					if (x == (j-1) * dimension) and ((0 <= y - i * dimension < dimension) or (0 < (y + dimension) - i * dimension < dimension)):
						x_update = 0
	return x_update, y_update

def play():
	pygame.init()
	screen = pygame.display.set_mode((width,height))
	pygame.display.set_caption("Pac Man v1.0")
	clock = pygame.time.Clock()
	x, y = 14*dimension, 17*dimension
	x_update, y_update = 0,0
	direction = None

	'''
	x_ghost1, y_ghost1 = 0,0
	x_ghost2, y_ghost2 = 0,0
	x_ghost3, y_ghost3 = 0,0
	x_ghost4, y_ghost4 = 0,0
	'''


	running = True
	while running:
		for event in pygame.event.get():
			if event. type == pygame.QUIT:
				running = False
			x_update, y_update, direction = movement(event,x_update,y_update,direction)
		# if len(directions) > 2:
		# 	del directions[0]
		x_update, y_update = stop(x,y,x_update,y_update,direction)
		x += x_update
		y += y_update
		grid(screen,width,height)
		x, y = tunnel(x,y,screen)
		
		pacman(screen,x,y)
		ghosts(screen)
		


		pygame.display.update()
		clock.tick(15)

	pygame.quit()
play()

'''
    Ghost — The Ghost class contains the different behaviour that the different ghosts have in the Pac-Man game. 
    		There are three distinct modes a ghost can be in: chase, scatter and frightened.
    ChaseBehaviour — The ChaseBehaviour interface is used to define different ghostly behaviours during the chase mode of the Pac-Man game.
    				 In chase mode, the ghosts will have different behaviours associated with their personalities.
    ChaseAggressive — The ChaseAggressive class contains the behaviour of a ghost in the Pac-Man game. 
    				  In chase mode, the ghost chases aggressively and will usually take the shortest route to you, and tends to follow.
    ChaseAmbush — The ChaseAmbush class contains the behaviour of a ghost in the Pac-Man game. 
    			  In chase mode, the ghost will attempt to ambush Pac-Man. The ghost tends to take a more wounding way towards Pac-Man with deadly effect.
    ChasePatrol — The ChasePatrol class contains the behaviour of a ghost in the Pac-Man game. 
    			  In chase mode, the ghost patrols around his designated block by default, only chasing Pac-Man if he comes near enough.
    ChaseRandom — The ChaseRandom class contains the behaviour of a ghost in the Pac-Man game. 
    			  In chase mode, the ghost will move in a random manner around the board and is not much of a threat.
'''