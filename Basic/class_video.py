class Video():
	def __init__(self):
		self.title = title
		self.link = link

	def read_video(self):
		print("-----")
		self.number_video = int(input("Insert numbers videos:"))
		for i in range(self.number_video):	
			self.title = input("Insert title of video" + str(i+1))
			print("Video" ,i,": Title of video", self.title)
			self.link= input("Insert link of video" + str(i+1))
			print("Video" ,i,": Link of video", self.link)

	# def print_video():
# def read_video():
# 	print("-----")
# 	number_video = int(input("Insert numbers videos:"))
# 	print("-----",str(number_video))
# 	for i in range(number_video):
# 		title = input("Insert title of video" + str(i+1))
# 		print("Video" ,i,": Title of video", title)
# 		link= input("Insert link of video" + str(i+1))
# 		print("Video" ,i,": Link of video", link)

def main():
	print("-----")
	read_video(self)
main()