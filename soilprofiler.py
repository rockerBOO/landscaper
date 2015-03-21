
import landscaper.web as web
from collections import OrderedDict
#import unicode

#url = 'http://casoilresource.lawr.ucdavis.edu/gmap/get_mapunit_data.php?lat=42.08026039284663&lon=-72.54465579986572'

#html = web.scrape(url)



def mapRecords(soup):
	results = {}

	headings = OrderedDict()
	records = OrderedDict()

	# Map attribute
	i = 0
	for x in soup.select(".heading"):
		headings[i] = x.string.strip()[:-1]
		i += 1

	# Map property
	i = 0
	for y in soup.select(".record"):
		records[i] = y.string.strip()

		i += 1

	# Map to attribute: property
	for i, heading in headings.items():
		results[heading] = records[i]

	return results


soup = web.soup(open('./data/mapunit.html', encoding="utf-8"))

records = mapRecords(soup)


print(records)