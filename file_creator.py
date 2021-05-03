import time
class Note:
	def __init__(self):
		gtmtime=time.gmtime(time.time())
		year = str(int(gtmtime.tm_year))
		month=str(int(gtmtime.tm_mon))
		day=str(int(gtmtime.tm_mday))
		hour=str(int(gtmtime.tm_hour))
		minutes=str(int(gtmtime.tm_min))
		seconds=str(int(gtmtime.tm_sec))
		self.code=year+month+day+hour+minutes+seconds;			
	
	def write_to_file(self, title):
		self.title=title;
		file = open(self.code+" - "+self.title+".md", "w")
		file.write("---\n")
		file.write("id: "+self.code+"\n")
		file.write("title: "+self.title+"\n")
		file.write("keywords: \n"+"#keyword1\n");
		file.write("---\n")
		file.write("Zettel Link: [[zettel_url]]\n")
		file.write("Citation - Your idea\n")
		file.write("Outside Link: "+ "[VK](https://vk.com/)\n")
		file.close()
		
