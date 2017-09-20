import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))
 
pygame.display.set_caption('Imagine World of Mine')
done = False
doge = pygame.image.load('Doge.png')
doge = pygame.transform.scale(doge,(60,60))
font = pygame.font.SysFont("Cordia",20)
hp = font.render("HP",True,(255,255,255))
energy = font.render("En",True,(255,255,255))
screen.fill((0,0,0))

x = 80
y=250
def checkCollision(a,w):

	if a.x >= w.x or a.x <= w.right:
		Iscollision = True
	else:
		Iscollision = False

	return Iscollision


clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]: y -=3
	if pressed[pygame.K_DOWN]: y+=3
	if pressed[pygame.K_LEFT]: x-=3
	if pressed[pygame.K_RIGHT]: x+=3
	
	
	
	screen.fill((0,0,0))		
	rect = doge.get_rect()
	rect = rect.move((x,y))
	screen.blit(doge,rect)
	
	pygame.draw.rect(screen,(255,0,0),pygame.Rect(50,30,200,10))	
	pygame.draw.rect(screen,(0,255,0),pygame.Rect(50,50,200,10))
 
	screen.blit(hp,(25,30))	
	screen.blit(energy,(25,50))
	
	pygame.display.flip()
	clock.tick(60)


		