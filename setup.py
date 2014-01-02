

class plist:

	def __init__(self, user, directory, script, hour, plistname):

		file_string ="""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>%s</string>
    <key>OnDemand</key>
    <true/>
    <key>RunAtLoad</key>
    <false/>
    <key>UserName</key>
    <string>%s</string>
    <key>Program</key>
    <string>python %s/%s</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>%s</integer>
        <key>Minute</key>
        <integer>30</integer>
    </dict>
</dict>
</plist>""" % (plistname, user, directory, script, hour)

		self.output = file_string

		self.plistname = plistname

	def writeout(self):

		out = open("%s.plist" % self.plistname, "w")

		for line in self.output:

			out.write(line)

		out.close()

		return 0

	def load(self):

		import os

		fname = "%s.plist" % self.plistname

		command = "launchctl load %s" % fname

		os.system(command)

		return 0









import platform, os, time
arch = platform.system()



if arch == 'Darwin':
	# this is a mac, create a plist

	print "installing on mac"

	# get install directory
	directory = os.getcwd()

	# make directory to store
	print "Making directory /Library/Desktop Pictures/APOD"
	os.system("mkdir '/Library/Desktop Pictures/APOD'")




	# get correct time to run

	zone_offset = 5 - time.timezone

	if zone_offset >= 0:

		string_time = str( abs(zone_offset) )

		if len(string_time) == 1 and string_time :
			hour = "0%i" % (zone_offset)

		elif len(string_time) == 2:
			hour = "%i" % (zone_offset)

	else:
		zone_offset = 24 + zone_offset
		hour = "%i" % (zone_offset)

	# get username
	user = os.getlogin()

	# script name
	script = "apodgrabber.py"

	# file text
	plistname = "local.apod"
	pl = plist(user, directory, script, hour, plistname)

	# write file
	pl.writeout()

	# load plist
	pl.load()





else:
	print "Sorry, only have mac support at the moment."

