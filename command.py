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
IPIlist = []

##
## methods called in script
def initial_search(term):
	# find search box on unigene page
	# enter term, get resulting url
	values = {'term' : term } # from html, defined as search term, specifies where and what to put in search box
	data = urllib.urlencode(values) # makes input usable
	request = urllib2.Request("http://www.ncbi.nlm.nih.gov/unigene/", data, headers)# sends post request
	response = urllib2.urlopen(request) # gets url from search
	#print response # just checking
	return response 

def analyze_search(search_page):
	page = search_page.read()
	soup = BeautifulSoup(page)
	#print soup
	#if "No items found" in str(soup.find('title')):
	#	return False
	#print soup.title
	rslt = str(soup.find("div", { "class" : "rslt" }))
	#print 'rslt = ', rslt
	substring_start = rslt.find('href') + 6
	substring_end = rslt.find('"', substring_start)
	link = rslt[substring_start : substring_end]
	return link
	# finds link to unigene page

def scrape_data_final(url):
	# find NP_
	#print url
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	table = soup.find('table', { 'class' : 'DataTable' })
	#print table
	for tr in table.findAll('tr'):
		if 'M. musculus' in str(tr):
			column = tr
			break
	if not 'M. musculus' in str(table): 
		for tr in table.findAll('tr'):
			if 'H. sapiens' in str(tr):
				column = tr
				break
	if not 'H. sapien' in str(table) and not 'M. musculus' in str(table):
		return False
	else:
		a = column.find('a')
		a_string = str(a)
		substring_start = a_string.find('NP')
		return a_string[substring_start : -5]


##
## actual command part

# creates an array of all terms-to-be-searched and takes underscores out of them to maket them search-friendly
for x in range(1, 1083):
	bcarray.append((bcsheet.cell( x, 3).value).replace('_', ' '))

for term in bcarray:
	unigene = initial_search(term)
	#print unigene
	searchresults = analyze_search(unigene)
	print 'search results = ',  searchresults
	if len(searchresults) == 0 :
		NPlist.append('')
	else:
		golden_hyde = scrape_data_final('http://www.ncbi.nlm.nih.gov' + searchresults)
		if golden_hyde == False:
			NPlist.append('')
		else:
			NPlist.append(golden_hyde)
	print term

# writes the GeneID and Accession number in a new workbook
for x in range(len(NPlist)):
	sheet1.write(0, x, NPlist[x]) 

for x in range(1, 1083):
	IPIlist.append((bcsheet.cell( x, 4).value))

for x in range(0, 1082):
	sheet1.write(2, x, IPIlist[x])
	
resultbook.save('updated_protein_IDs.xls') # saves workbook --- !!! DONE !!! ---
