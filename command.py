# Peter Flock<3 // 2013

# lots-o-modules!!!
from mmap import mmap, ACCESS_READ 	# I forget why it's here, it's safer to leave it though
from xlrd import open_workbook		# Reading contents of excel spreadsheets
from xlwt import Workbook		# writing and saving excel docs
import re				# I don't remember, k? seriously though what if I need it
from bs4 import BeautifulSoup 		# scrape html docs
import urllib 				# send post and get requests to a url
import urllib2 				# open urls as html docs

# bunch of constants and declarations 
unigeneurl =  'http://www.ncbi.nlm.nih.gov/UniGene/'
# in case the server wants an actual browser ID 
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent }
# non web stuff
bcbook = open_workbook('Proteins-010-0103-R-A01.xls')
bcsheet = bcbook.sheet_by_index(0)
bcarray = []
resultbook = Workbook()
sheet1 = resultbook.add_sheet('Sheet1')
gene_ID_Access_num = {}

##
## actual command part

# creates an array of all terms-to-be-searched and takes underscores out of them to maket them search-friendly
for x in range(1, 1083):
	bcarray.append((bcsheet.cell( x, 3).value).replace('_', ' '))

for value in bcarray():
	unigene = initial_search(value)
	searchresults = analyze_search(unigene)
	if searchresults = False:
		geneID_Access_num.append('')
	else:
		final_page = scrape_unigene('http://www.ncbi.nlm.nih.gov' + searchresults)
		golden_hyde = scrape_data_final(final_page)
		geneID_Access_num.append(golden_hyde)

# writes the GeneID and Accession number in a new workbook
for x in range(gen_ID_Access_num.len):
	sheet1.write(0, x, gen_ID_Access_num[x]) # doesn't work, look at array[array] workings
	
resultbook.save('updated_protein_IDs.xls') # saves workbook


##
## methods called in script
	
def initial_search(term):
	# find search box on unigene page
	# enter term, get resulting url
	values = {'search' : term } # from html, defined as search term, specifies where and what to put in search box
	data = urllib.urlencode(values) # makes input usable
	request = urllib2.Request(unigeneurl, data, headers) # sends post request
	response = urllib2.urlopen(request) # gets url from search
	print response # just checking
	return url 

def analyze_search(search_page):
	page = urllib2.urlopen(search_page)
	soup = BeautifulSoup(page)
	if "No items found" in str(soup.find('title')):
		return False
	rslts = soup.find_all(match_class(["rslt"]))
	# could maybe replace ^ w/ rslt = soup.find("div", { "class" : "rslt" })
	rslts = str(rslts)
	substrt = rslts.find('href') + 6
	link = rslts[substrt: rslts.find('"', substrt)]
	return link
	# finds all the search results dspld on the page
	# gotta look for first result, return null if no results

def scrape_unigene(url):
	# search table for M. Musculus
	# find linkable NP_ on that line, find 'Protein Sequence' link
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	# find M. Musculus in 'PortletBox' class and then navigate to the first list item and find the href linked to "protein sequence"
	return finalurl

def scrape_data_final(url):
	# find NP_ and Gene ID
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	rslt = soup.find("div", { "class" : "itemid" })
	# test 'print str(rslt)' to see the output then search for NP_ accordingly
	# if no M. Musculus entry look for H. Sapien
	result = NP
	return result

def match_class(target):                                                        
#    def do_match(tag):                                                          
        classes = tag.get('class', [])                                          
        return all(c in classes for c in target)                                
#    return do_match                                 
