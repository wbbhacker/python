import urllib
import urllib2

import urllib
import urllib2

values = {'username':'27687682@qq.com','password':'22223'}

data = urllib.urlencode(values) 

url = 'www.baiud.com'

request = urllib2.Request(url,data)

response = urllib2.urlopen(request)

print response.read()
