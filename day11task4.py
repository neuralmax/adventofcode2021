import pandas as pd
import statistics
from random import randint
import pygame, sys
from pygame.locals import *

#with open('data.txt','r') as f:
#with open('sample.txt','r') as f:
	#data=f.readlines()
#data=[d.strip() for d in data]
wx=wy=500
pygame.init()
windowSurface = pygame.display.set_mode((wx,wy),0,32)

dat=[[randint(0,9) for x in range(wx)] for y in range(wy)]
def plot(dat):
	s=''
	i=[[str(n) for n in lin] for lin in dat]
	i=[[n if int(n)>0 else '.' for n in lin] for lin in i]
	for d in i:
		s+=''.join(d)+'\n'
	print(s)
	#print('')

nbrs=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
plot(dat)
flashes=0
stepFlashes=0
step=0
colors=[
[79,79,79],
[80,78,16],
[0,78,78],
[0,77,14],
[83,20,78],
[100,20,11],
[86,15,8],
[0,16,98],
[0,13,78],
[0,0,0],
]
pygame.display.set_caption('dumbo Octopus')
frame=0
flashData=[]
running=True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	stepFlashes=0
	dat=[[n+1 for n in lin] for lin in dat]
	dat=[[n+1 if randint(0,9)==0 else n for n in lin] for lin in dat]
	flashed=[[0 for n in lin] for lin in dat]
	newFlashes=1
	while newFlashes>0:
		newFlashes=0
		for x in range(wx):
			for y in range(wy):
				if dat[x][y]>9 and flashed[x][y]==0:
					#dat[x][y]=0
					flashed[x][y]+=1
					newFlashes+=1
					stepFlashes+=1
					for n in nbrs:
						nx=x+n[0]
						ny=y+n[1]
						if nx>=0 and nx<wx and ny>=0 and ny<wy:
							dat[nx][ny]+=1
		flashes+=newFlashes
	dat=[[0 if n>9 else n for n in lin] for lin in dat]
	#print('step',step+1,'stepFlashes',stepFlashes)
	#plot(dat)
	flashData.append(stepFlashes)
	step+=1
	if step%(6*10)==0:

		windowSurface.fill((0,0,0))
		for x in range(wx):
			for y in range(wy):
				#clr=colors[dat[x][y]]
				clr=(dat[x][y]*25,dat[x][y]*25,dat[x][y]*25)
				#clr=(dat[x][y]*25,abs(5-dat[x][y])*50,(9-dat[x][y])*25)
				windowSurface.set_at((x,y),clr)
		pygame.display.update()
		pygame.image.save(windowSurface,'frame'+str(frame)+'.png')
		pygame.display.set_caption('dumbo Octopus '+str(frame))
		frame+=1
		if frame>100:running=False

print(flashes)
with open('flashData.txt','w') as f:
	for d in flashData:
		f.write(str(d)+'\n')
