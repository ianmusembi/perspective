# Photomanipulator
# Author : Ian Musembi


# pointilismFunctions.py

'''
Helper functions for redrawing images using pointilism technique
'''


import random

def getRGBLimits( r, g, b, points_per_pixel = 15) :

	'''
	rgb limits store integer values of the number of red, blue and green points
	to be drawn per pixel. THe rgb limits vary in correspondence to the rgb values
	of a pixel
	'''

	red_lim = int((r/((r + g + b)+ 1)) * points_per_pixel)

	green_lim = int((g/((r + g + b)+ 1)) * points_per_pixel)

	blue_lim = int((b/((r + g + b)+ 1)) * points_per_pixel)

	return red_lim, green_lim , blue_lim


def getRelativeRowColumn (row, col, original_dimensions, new_dimensions, width_factor,
			  			  height_factor, xSpacing  = 0, ySpacing = 0) -> list[int , int] :

	'''
	Param - original_dimensions is a tuple == (original_width, original_height)
	Param - new_dimensions is a tuple == (new_width, new_height)
	'''

	'''calculates column and row position of the resized image
	relative to the original image pixel '''
	src_width, src_height = original_dimensions
	resized_width, resized_height = new_dimensions
	relative_col = int(col * (resized_width/src_width))
	relative_row = int(row * (resized_height/src_height))

	''' the position range for redrawing the original image pixels onto the screen'''
	new_col = (relative_col * width_factor) + resized_width + xSpacing
	new_row = relative_row * height_factor + ySpacing

	'''randx and randy are used to slightly randomize the position
		of the points used to draw the image while still keeping them
		within their relative positions in the image. '''
	randx = random.randint((new_col), (new_col + (width_factor)) )
	randy = random.randint((new_row - (height_factor) ), (new_row))

	return randx, randy