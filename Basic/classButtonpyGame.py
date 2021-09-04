import pygame

class TextButton():

	def __init__(self, text, position):
		self.text = text
		self.position = position
		# print(text, position)

	def is_mouse_on_text(self):
		pos_mouse_x, pos_mouse_y = pygame.mouse.get_pos()
		on_text = False
		if pos_mouse_x>self.position[0] and pos_mouse_x<self.position[0]+self.pos_rect[2] and pos_mouse_y>self.position[1] and pos_mouse_y<self.position[1]+self.pos_rect[3]:
			on_text = True
		return on_text

	def draw_text(self):
		
		font_text = pygame.font.SysFont("San", 30)
		render_text = font_text.render(self.text, True, (0,0,0))	
		self.pos_rect = render_text.get_rect()
		screen.blit(render_text, self.position)

		if self.is_mouse_on_text():
			render_text = font_text.render(self.text, True, (0,0,255))	
			screen.blit(render_text, self.position)
		else:
			pass

		
	def draw_line_text(self):
		if self.is_mouse_on_text():
			pos_lineUdertext = self.find_pos_2point_lineundertext()
			pygame.draw.line(screen, BLUE, pos_lineUdertext [2], pos_lineUdertext [3])
			# print("-----",pos_lineUdertext)

	def find_pos_2point_lineundertext(self):
		# print("=====", self.d3)
		d1 = (self.position[0],self.position[1])
		d2 = (self.position[0]+self.pos_rect[2], self.position[1])
		d3 = (self.position[0]+self.pos_rect[2], self.position[1]+self.pos_rect[3])
		d4 = (self.position[0],self.position[1]+self.pos_rect[3])
		pos_four_rectangle =(d1, d2, d3, d4)
		return pos_four_rectangle



pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Sofe VuNghiXuan')
running = True
clock = pygame.time.Clock()

BLUE = (0,0,255)
GREEN = (0, 200, 0)
WHITE = (255,255,255)

press_name = "Press click"
press_pos = (50,50)
bnt_press = TextButton(press_name, press_pos)

while running:		
	clock.tick(60)
	screen.fill(WHITE)

	bnt_press.draw_text()
	bnt_press.draw_line_text()

	# print(bnt_press.find_pos_2point_lineundertext())
	
	# if bnt_press.is_mouse_on_text():
	# 	bnt_press.draw_line_text()
		# bnt_press.draw_line_text()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:			
			if event.button ==1:
				if bnt_press.is_mouse_on_text():
					pass #print(bnt_press.is_mouse_on_text())
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()