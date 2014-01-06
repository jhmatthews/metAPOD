import os, sys
import selenium_apod as sel 
from urllib import FancyURLopener

class MyOpener(FancyURLopener):
	version = "APOD grabber FancyURLopener"


class ascript:

	'''class which contains command for setting background'''

	def __init__(self, filename):

		self.command = '/usr/bin/osascript<<END\ntell application "Finder"\n\
						set desktop picture to POSIX file "%s"\n\
						end tell\nEND' % filename



class APOD():

	'''class with functions for getting images'''

	def get_image_url(self, url):

		'''
		gets url from NASA APOD webpage

		:INPUT:
			url 		string
						url to search 
						e.g. "http://apod.nasa.gov/apod/astropix.html

		:OUTPUT:
			image 		string 
						image url to fetch
		'''

		import urllib2

		file_name = url.split('/')[-1]

		u = urllib2.urlopen(url)
	
		for line in u:

			data = line.split()

			if len(data) > 0:
				if data[0] == "<a" and data[1][:4] == "href" and data[1][6:11] == "image":

					print data
					image = "http://apod.nasa.gov/apod/%s" % data[1][6:-2]

		
		return image


	def get_image (self, url):

		'''
		gets image at a given url

		:INPUT:
			url 		string
						url location of image 

		:OUTPUT:
			filename 	string 
						local image filename
		'''

		myopener = MyOpener()

		filename = "images/%s" % url[37:]

		retrieve = myopener.retrieve(url, filename)

		return filename

	def set_picture (self, filename):
		
		'''
		sets picture as desktop background

		:INPUT:
			filename 	string 
						local image filename

		:OUTPUT:
			0			success
		'''

		cur_dir = os.getcwd()

		fname = "%s/%s" % (cur_dir, filename)

		command = ascript(fname).command

		print command 

		os.system ( command )

		return 0




# create grabber, APOD class instance
grabber = APOD()

# get image url
img = grabber.get_image_url ("http://apod.nasa.gov/apod/astropix.html")

# get filename (locally) of image
filename = grabber.get_image(img)

# set as background
grabber.set_picture(filename)

# all done


