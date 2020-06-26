import pygame
from random import randint 

mul = 2
width = 8 * 28 * mul											#standard Pac-Man dimensions 
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
			x_update = -dimension
			y_update = 0
			direction = 'left'
		elif event.key == pygame.K_RIGHT:
			x_update = dimension
			y_update = 0
			direction = 'right'
		elif event.key == pygame.K_UP:
			x_update = 0
			y_update = -dimension
			direction = 'up'
		elif event.key == pygame.K_DOWN:
			x_update = 0
			y_update = dimension
			direction = 'down'
	return x_update, y_update, direction	


def tunnel(x,y):
	if x == 27 * dimension and y == 14 * dimension:
		x = dimension 
	elif x == 0 and y == 14 * dimension:
		x = 26 * dimension
	return x, y

def stop(x,y,x_update,y_update,direction):
	for i in range(len(map_)):
		for j in range(len(map_[i])):
			if not (i == 14 * dimension and j == 0) or (i == 14 * dimension and j == 27 * dimension):
				if map_[i][j] == 0:
					if x == j * dimension and y == i * dimension:
						x_update, y_update = 0,0				 

	# stop function depending on the direction to be implemented
	return x_update, y_update

def play():
	pygame.init()
	screen = pygame.display.set_mode((width,height))
	pygame.display.set_caption("Pac Man v1.0")
	clock = pygame.time.Clock()
	x, y = 14*dimension, 17*dimension
	x_update, y_update = 0,0
	direction = None






	running = True
	while running:
		for event in pygame.event.get():
			if event. type == pygame.QUIT:
				running = False
			x_update, y_update, direction = movement(event,x_update,y_update,direction)
		x_update, y_update = stop(x,y,x_update,y_update,direction)
		x += x_update
		y += y_update
		grid(screen,width,height)
		x, y = tunnel(x,y)
		
		pacman(screen,x,y)
		ghosts(screen)
		








		pygame.display.update()
		clock.tick(5)

	pygame.quit()
play()

# 224 x 288, so dividing each value by eight yields a grid that is 28 x 36 
