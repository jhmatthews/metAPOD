import os, sys
import selenium_apod as sel 
from urllib import FancyURLopener

class MyOpener(FancyURLopener):
	version = "APOD grabber FancyURLopener"


class ascript:

	def __init__(self, filename):

		self.command = '/usr/bin/osascript<<END\ntell application "Finder"\n\
						set desktop picture to POSIX file "%s"\n\
						end tell\nEND' % filename



class APOD():

	def get_image_url(self, url):

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

		myopener = MyOpener()

		filename = url[37:]

		retrieve = myopener.retrieve(url, filename)

		return filename

	def set_picture (self, filename):

		

		fname = "/Users/jamesmatthews/Downloads/my-APOD-grabber/%s" % filename

		command = ascript(fname).command

		os.system ( command )

		return 0







grabber = APOD()

img = grabber.get_image_url ("http://apod.nasa.gov/apod/astropix.html")

filename = grabber.get_image(img)

grabber.set_picture(filename)



