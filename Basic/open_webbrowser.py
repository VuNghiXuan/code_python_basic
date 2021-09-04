import webbrowser
class Video:
	def __init__(self, title, link ):
		self.title = title
		self.link = link
		# self.seen = False

	def open(self):
		webbrowser.open(self.link)
		# self.seen = True

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

def read_video():
	title = input("Enter title of video:") + "\n"
	link = input("Enter title of link:") + "\n"
	video = Video(title, link)
	# print("[[[[[",video.title)
	return video
	# total_video = int(input("Enter how many videos: "))
	# title = input("Enter title video: ")
	# link = input("Enter link video: ")
	# video = Video(title, link)
	# return video

def read_videos():
	total = int(input("Enter number videos: "))	
	videos = []
	for i in range(total):
		vids = read_video() 
		# print ("=====" + vids.title)
		# videos.append(vids[i]) # vids[i] sai do vids là mảng 1 chiều
		videos.append(vids) 
	return videos

	# total_video = int(input("Enter how many videos: "))
	
	# videos=[]
	# for i in range(total_video):
	# 	print ("Video ", i+1 )		
	# 	vid = read_video()
	# 	videos.append(vid)
	# return videos
def write_filetxt(videos, file):
	total = len(videos)

	# print("-----ugu---", str(f), str(total))

	# with open(f,"w") as file:
	file.write(str(total) + "\n")
	for i in range(total):
		file.write(videos[i].title) #+ "\n"
		file.write(videos[i].link)

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

def print_video(video):
	# total = len(video)
	# print ("----------" + total)
	for i in range(len(video)):
		print("Title video " + str(i + 1) + ": " + video[i].title)
		print("Link video " + str(i + 1) + ": " + video[i].link)

def print_video_fromTxt(video):
	# total = len(video)
	# print ("----------" + total)
	for i in range(len(video)):
		print("Title video " + str(i + 1) + ": " + video[i].title, end = "")
		print("Link video " + str(i + 1) + ": " + video[i].link, end = "")

def read_1_playlist():
	playlist_name = input("Enter playlist' name: ") + "\n" #backward slash "\": ngã về phái sau, forward slash "\"
	playlist_description = input("Enter description of playlist: ") + "\n"
	playlist_rating = input("Enter rating (choice 1-5): ") + "\n"
	videos = read_videos() 
	playlist_video = Playlist(playlist_name, playlist_description, playlist_rating, videos)
	return playlist_video

def write_1_Playlist_file(playlist, file):
	with open(file, "w") as file:
		file.write(playlist.name )#+ "\n"
		file.write(playlist.description)
		file.write(playlist.rating)
		# file.write(playlist.videos + "\n")
		write_filetxt(playlist.videos, file)
		# print("Write txt succesfully!!!")

def read_1_playlist_from_txt(file):
	# playlist = []
	with open(file, "r") as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_video = read_filetxt(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_video)
	return playlist

def print_1_playlist(playlist_from_txt):
	# total = len(playlist_from_txt)
	# for i in range(total):
	print("==============")
	print("Playlist_name: " + playlist_from_txt.name)
	print("playlist_description: " + playlist_from_txt.description)
	print("playlist_rating: " + playlist_from_txt.rating)
	# print("Playlist_name: " + playlist_from_txt.name)
	video = playlist_from_txt.videos
	print_video_fromTxt(video)
	print("Succesfully!!!")

def show_menu():
	print("\n+----Menu playlist video----+")
	print("+ Option 1: Create playlist +")
	print("+ Option 2: Show playlist   +")
	print("+ Option 3: Play video      +")
	print("+ Option 4: .......         +")
	print("+ Option 5: .......         +")
	print("+ Option 6: .......         +")
	print("+ Option 7: Save or Exit    +")
	print("+------------OoO------------+")

def select_range_number(prompt, min, max):
	choice = input (prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max: #"choice.isdigit()", ko phải là số
		choice = input (prompt)
	choice = int(choice)
	return choice

def play_video(playlist):
	print_video_fromTxt(playlist.videos)
	total_videos = len(playlist.videos)
	choice = select_range_number("Choice range number from (1-" + str(total_videos) + "): " , 1, total_videos)
	print("You choice Video of name: " + playlist.videos[choice-1].title + ". Linlk of video: " + playlist.videos[choice-1].link, end = "")
	# webbrowser.open(playlist.videos[choice-1].link, new = 2 ) #new = 2 : ko mở Tab mới
	playlist.videos[choice-1].open()
	# playlist.videos[choice-1].open()

def choice_option_menu():
	try:		
		file = "data.txt"
		playlist = read_1_playlist_from_txt(file) #Erros when the file data is not data
		print("Loaded data succesful!!!")
	except:
		print("Wellcom you into playlist video")

	while True:
		show_menu()
		choice = select_range_number("Choice range number from (1-7): ", 1,7)	
		if choice == 1:			
			playlist = read_1_playlist()
			input("\nPress enter to continue.\n")
			# break
		elif choice == 2:
			print_1_playlist(playlist)
			input("\nPress enter to continue.\n")
			# break
		elif choice == 3:
			play_video(playlist)
			break
		elif choice == 7:
			write_1_Playlist_file(playlist, file)
			print("Save as file succesfull !!!")
			break
		# else:			
		# 	print("Wrong input and Exit!")
		# 	break

def main():
	# file = "data.txt"
	# vids = read_videos()s
	# # print ("----------" +  str(len(vids))
	# write_filetxt(vids, file)

	# videos = read_filetxt(file)

	# print_video_fromTxt(videos)

	# Kết thúc bài 50
	# playlist = read_1_playlist()
	# write_1_Playlist_file(playlist, file)
	# playlist_readfrom_txt = read_1_playlist_from_txt(file)
	# print_1_playlist(playlist_readfrom_txt)
	# Begin bài 51
	# select_range_number("Nhap:Choice range number from (1-7): ", 1, 7)
	choice_option_menu()
		

main()