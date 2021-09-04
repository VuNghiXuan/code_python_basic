# Phím tắc:
#   - Đổi hàng loạt biến: Ctrl+D (n lần), tương ứng số lần thay đổi
import webbrowser
import pygame
class Video:
	def __init__(self, title, link ):
		self.title = title
		self.link = link
		self.seen = False

	def open(self):
		webbrowser.open(self.link)
		self.seen = True
		
class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

class TextButton():

	def __init__(self, text, position):
		self.text = text
		self.position = position
		# print(text, position)

	def is_mouse_on_text(self):
		pos_mouse_x, pos_mouse_y = pygame.mouse.get_pos()
		
		if pos_mouse_x>self.position[0] and pos_mouse_x<self.position[0]+self.pos_rect[2] and pos_mouse_y>self.position[1] and pos_mouse_y<self.position[1]+self.pos_rect[3]:
			return True
		return False

	def draw_text(self):
		
		font_text = pygame.font.SysFont("San", 25)
		render_text = font_text.render(self.text, True, (0,0,0))	
		self.pos_rect = render_text.get_rect()
		# screen.blit(render_text, self.position)

		if self.is_mouse_on_text():
			render_text = font_text.render(self.text, True, (0,0,255))	
			screen.blit(render_text, self.position)
			pos_lineUdertext = self.find_pos_2point_lineundertext()
			pygame.draw.line(screen, BLUE, pos_lineUdertext [2], pos_lineUdertext [3])
		else:
			screen.blit(render_text, self.position)
		
	# def draw_line_text(self):
	# 	if self.is_mouse_on_text():
	# 		# pos_lineUdertext = self.find_pos_2point_lineundertext()
	# 		# pygame.draw.line(screen, BLUE, pos_lineUdertext [2], pos_lineUdertext [3])
	# 	else:
	# 		# pos_lineUdertext = self.find_pos_2point_lineundertext()
			# print("-----",pos_lineUdertext)

	def find_pos_2point_lineundertext(self):
		# print("=====", self.d3)
		d1 = (self.position[0],self.position[1])
		d2 = (self.position[0]+self.pos_rect[2], self.position[1])
		d3 = (self.position[0]+self.pos_rect[2], self.position[1]+self.pos_rect[3])
		d4 = (self.position[0],self.position[1]+self.pos_rect[3])
		pos_four_rectangle =(d1, d2, d3, d4)
		return pos_four_rectangle

def read_1video_formTxt(f):	
	title = f.readline()
	link = f.readline()
	video = Video(title, link)
	return video	

def read_filetxt(file):	
	videos = []
	# with open(f,"r") as file:
	total_video = int(file.readline())
	# print("Number of videos by use enter: " + str(total_video))
	for i in range(total_video):
		video = read_1video_formTxt(file)
		videos.append(video)
	return videos

def read_1_playlist_from_txt(file):
	# playlist = []
	with open(file, "r") as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_video = read_filetxt(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_video)
	return playlist


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Sofe VuNghiXuan')
running = True
clock = pygame.time.Clock()

BLUE = (0,0,255)
GREEN = (0, 200, 0)
WHITE = (255,255,255)




#------>assign btn_playlist
file = "data.txt"

playlist = read_1_playlist_from_txt(file)

# seach google "remove newline from string python"
btn_playlist = playlist.name.rstrip("\n") # rstrip("\n") hoac rstrip(): bỏ ký tữ xuống dòng

btn_playlist_pos = (50,50)
bnt_press = TextButton(btn_playlist, btn_playlist_pos)
#assign btn_playlist <------

#------>assign btn_videos =title video
btn_list_videos = []

total_video = len(playlist.videos)
margin = 30 # margin: lề
for i in range(total_video):
	btn_videos_pos = (btn_playlist_pos[0] + 300, btn_playlist_pos[0]+(margin*i))
	btn_list_video = TextButton(str(i+1) + ". "+ playlist.videos[i].title.rstrip("\n"), btn_videos_pos)#margin: là khoảng cách 50
	btn_list_videos.append(btn_list_video)


while running:		
	clock.tick(60)
	screen.fill(WHITE)

	bnt_press.draw_text()
	# bnt_press.draw_line_text()
	

	# show list viseos
	for i in range(len(btn_list_videos)):
		btn_list_videos[i].draw_text()
		# btn_list_videos[i].draw_line_text()
	# print(bnt_press.find_pos_2point_lineundertext())
	
	# if bnt_press.is_mouse_on_text():
	# 	bnt_press.draw_line_text()
		# bnt_press.draw_line_text()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:			
			if event.button ==1:
				if bnt_press.is_mouse_on_text():
					print("you choice")
				for i in range(len(btn_list_videos)):
					if btn_list_videos[i].is_mouse_on_text():
						playlist.videos[i].open()

		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()