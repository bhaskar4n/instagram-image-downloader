#program to download images in instagram website.
#only required profile page web address
import json
import urllib.request
import urllib.request
import json
import re
import bs4 as bs
import urllib
from socket import timeout
#urllib.request.urlretrieve('https://instagram.fmaa1-2.fna.fbcdn.net/t51.2885-15/e35/16789245_1231140993619505_838931546701299712_n.jpg','imagge.jpg')
import requests

def run(weblink,f,flag,brk):
	print("Downloading all images")
	web_link = "https://www.instagram.com/"+str(weblink)
	while(flag == 0):
		page = requests.get(web_link)
		html_contents = page.text
		soup = bs.BeautifulSoup(html_contents, 'lxml')
		data  = soup.find_all("script")
		a = 0
		for i in data:
			#print(a,"###################################")
			#print(i)
			a = a+1
		jsondata = str(data[6])
		jd = str(jsondata[52:])
		data11 = str(jd[:-10])
		#print(data11)
		src_link = list()
		loader = list()
		mydict = json.loads(data11)
		for i in range(11,12):
			try:
				id = (mydict['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['id'])
				#print (id)
			except:
				print("Loading finished...")
		for i in range(12):
			f = f+1
			try:
				src = (mydict['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['display_src'])
			except:
				print("image address indetifying finished")

			if src in src_link:
				print("duplicate image link found")
				print("whole process finished")
				print("image downloading finished")
				brk = 1
			if brk != 0:
				break
			src_link.append(src)
			web_link = "https://www.instagram.com/"+str(weblink)+"/?max_id="+str(id)
			loader.append(web_link)
			print (f,"....",str(src))
			urllib.request.urlretrieve(str(src),str(f)+"_image.jpg")
		if brk != 0:
			break
		print(f," next..............................:",web_link)
run(str(input("enter the instagram profile name: ")),0,0,0)
