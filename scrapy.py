import urllib2

for x in xrange(3281,999999):
	url = 'http://www.cdnediser.com/formation/question/PERMISB/web-Q-image/Q{id}.jpg'
	url = url.replace ('{id}', str(x).zfill(6))
	#print url	
	try:
		#print url
		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		response = opener.open(url)
		#print response.code
		print url
		#print "I get a link"
	except urllib2.HTTPError as e:
		#print e.code
		#print "except"
		pass
print "End of Job"