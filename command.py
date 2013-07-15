# Peter Flock<3 // 2013

# lots-o-modules!!!
from mmap import mmap, ACCESS_READ 	# I forget why it's here, it's safer to leave it though
from xlrd import open_workbook		# Reading contents of excel spreadsheets
from xlwt import Workbook		# writing and saving excel docs
import re				# I don't remember, k? seriously though what if I need it
from bs4 import BeautifulSoup 		# scrape html docs
import urllib 				# send post and get requests to a url
import urllib2 				# open urls as html docs

#
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
NPlist = []

##
## actual command part

# creates an array of all terms-to-be-searched and takes underscores out of them to maket them search-friendly
for x in range(1, 1083):
	bcarray.append((bcsheet.cell( x, 3).value).replace('_', ' '))

for term in bcarray():
	unigene = initial_search(term)
	searchresults = analyze_search(unigene)
	if searchresults = False:
		NPlist`.append('')
	else:
		golden_hyde = scrape_data_final('http://www.ncbi.nlm.nih.gov' + searchresults)
		NPlist.append(golden_hyde)

# writes the GeneID and Accession number in a new workbook
for x in range(gen_ID_Access_num.len):
	sheet1.write(0, x, NPlist[x]) 
	
resultbook.save('updated_protein_IDs.xls') # saves workbook --- !!! DONE !!! ---


##
## methods called in script
	
def initial_search(term):
	# find search box on unigene page
	# enter term, get resulting url
	values = {'term' : term } # from html, defined as search term, specifies where and what to put in search box
	data = urllib.urlencode(values) # makes input usable
	request = urllib2.Request(unigeneurl, data, headers) # sends post request
	response = urllib2.urlopen(request) # gets url from search
	print response # just checking
	return response 

def analyze_search(search_page):
	page = search_page.read()
	soup = BeautifulSoup(page)
	if "No items found" in str(soup.find('title')):
		return False
	rslt = str(soup.find("div", { "class" : "rslt" }))
	substring_start = rslts.find('href') + 6
	link = rslts[substring_start: substring_end]
	return link
	# finds all the search results displayed on the page
#
# no longer necessary since IDGAF abt gene IDs, just getting NP
#def scrape_unigene(url):
	# search table for M. Musculus
	# find linkable NP_ on that line, find 'Protein Sequence' link
#	page = urllib2.urlopen(url)
#	soup = BeautifulSoup(page)
	# find M. Musculus in 'PortletBox' class and then navigate to the first list item and find the href linked to "protein sequence"
#	return finalurl

def scrape_data_final(url):
	# find NP_
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	table = soup.find('table', { 'class' : 'DataTable' })
	for tr in table.findAll('tr'):
		if 'M. musculus' in str(tr):
		column = tr
	# test 'print str(rslt)' to see the output then search for NP_ accordingly
	# if no M. Musculus entry look for H. Sapien
	return result

