# Peter Flock<3 //2013

from bs4 import BeautifulSoup   	# scrape html docs
import urllib 				# send post and get requests to a url
import urllib2 	

url = 'http://www.ncbi.nlm.nih.gov/unigene/?term=protease'
page = urllib2.urlopen(url)	
soup = BeautifulSoup(page)
term = 'protease'
unigeneurl =  'http://www.ncbi.nlm.nih.gov/UniGene/'
# in case the server wants an actual browser ID 
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent }

#for link in soup.find_all('a'):
#	print(link.get('href'))

print "|||||| THIS LINE IS FOR TESTING PURPOSES _ MOVE ALONG |||||||"


def match_class(target):                                                        
    def do_match(tag):                                                          
        classes = tag.get('class', [])                                          
        return all(c in classes for c in target)                                
    return do_match                                                             

#rslts = soup.find_all(match_class(["rslt"]))

#print rslts

#rslts = str(rslts)
#substrt = rslts.find('href') + 6

#link = rslts[substrt: rslts.find('"', substrt)]
#print link

# supposesed to get the url from entering the search term into the search bar, don't know what it actually does
values = {'term' : term } # from html, defined as search term, specifies where and what to put in search box
data = urllib.urlencode(values) # makes input usable
request = urllib2.Request(unigeneurl, data, headers) # sends post request
response = urllib2.urlopen(request) # gets url from search
print str(response)


#from master_script.py 'analyze_search' function, replaced by above and call to 'match_class'
#	results = soup.findAll('div', attrs={'class' : 'rslt'})
