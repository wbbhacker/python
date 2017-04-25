import urllib  
import urllib2  
 
url = 'http://www.server.com/login'

values = {'username' : 'cqc',  'password' : 'XXXX' }  
data = urllib.urlencode(values)  

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
headers = { 'User-Agent' : user_agent }  

request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  

page = response.read()