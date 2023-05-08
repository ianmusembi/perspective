import pygame

def invertPixel(mousePos , xRange, yRange, screen) :

	xPos = mousePos[0]
	yPos = mousePos[1]

	left = xRange[0]
	right = xRange[1]

	top = yRange[0]
	bottom = yRange[1]

	x2 = xPos + 100
	y2 = yPos + 100
	

	# keep xPos and x2 within the display surface
	if (xPos < left ) :
		xPos = left
		
	if (yPos < top ) :
		yPos = top

	if (y2 >  bottom) :	
		y2 = bottom
	
	if (x2 > right) :
		x2 = right
		
	
	for y in range(yPos,y2) :
		for x in range(xPos,x2) :
		
			(r,g,b,_) = screen.get_at((x,y))
			
			r1 = 255 - r
			g1 = 255 - g
			b1 = 255 - b
			a1 = 255
			screen.set_at ((x,y), (r1,g1,b1,a1))

			# pygame.display.update()
		# pygame.display.update()
	


def isInDisplayArea (mousePos , xRange : list[int], yRange : list[int]):

	xPos = mousePos[0]
	yPos = mousePos[1]

	left = xRange[0]
	right = xRange[1]

	top = yRange[0]
	bottom = yRange[1]

	return (
			xPos >= left and
	 		xPos <= right and
			yPos >= top and
			yPos <= bottom
			)